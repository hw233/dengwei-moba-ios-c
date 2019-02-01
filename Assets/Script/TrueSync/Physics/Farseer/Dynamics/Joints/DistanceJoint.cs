/*
* Farseer Physics Engine:
* Copyright (c) 2012 Ian Qvist
* 
* Original source Box2D:
* Copyright (c) 2006-2011 Erin Catto http://www.box2d.org 
* 
* This software is provided 'as-is', without any express or implied 
* warranty.  In no event will the authors be held liable for any damages 
* arising from the use of this software. 
* Permission is granted to anyone to use this software for any purpose, 
* including commercial applications, and to alter it and redistribute it 
* freely, subject to the following restrictions: 
* 1. The origin of this software must not be misrepresented; you must not 
* claim that you wrote the original software. If you use this software 
* in a product, an acknowledgment in the product documentation would be 
* appreciated but is not required. 
* 2. Altered source versions must be plainly marked as such, and must not be 
* misrepresented as being the original software. 
* 3. This notice may not be removed or altered from any source distribution. 
*/
#pragma warning disable 0162

using System.Diagnostics;

namespace TrueSync.Physics2D
{
    // 1-D rained system
    // m (v2 - v1) = lambda
    // v2 + (beta/h) * x1 + gamma * lambda = 0, gamma has units of inverse mass.
    // x2 = x1 + h * v2

    // 1-D mass-damper-spring system
    // m (v2 - v1) + h * d * v2 + h * k * 

    // C = norm(p2 - p1) - L
    // u = (p2 - p1) / norm(p2 - p1)
    // Cdot = dot(u, v2 + cross(w2, r2) - v1 - cross(w1, r1))
    // J = [-u -cross(r1, u) u cross(r2, u)]
    // K = J * invM * JT
    //   = invMass1 + invI1 * cross(r1, u)^2 + invMass2 + invI2 * cross(r2, u)^2

    /// <summary>
    /// A distance joint rains two points on two bodies
    /// to remain at a fixed distance from each other. You can view
    /// this as a massless, rigid rod.
    /// </summary>
    public class DistanceJoint : Joint2D
    {
        // Solver shared
        private FP _bias;
        private FP _gamma;
        private FP _impulse;

        // Solver temp
        private int _indexA;
        private int _indexB;
        private TSVector2 _u;
        private TSVector2 _rA;
        private TSVector2 _rB;
        private TSVector2 _localCenterA;
        private TSVector2 _localCenterB;
        private FP _invMassA;
        private FP _invMassB;
        private FP _invIA;
        private FP _invIB;
        private FP _mass;

        internal DistanceJoint()
        {
            JointType = JointType.Distance;
        }

        /// <summary>
        /// This requires defining an
        /// anchor point on both bodies and the non-zero length of the
        /// distance joint. If you don't supply a length, the local anchor points
        /// is used so that the initial configuration can violate the constraint
        /// slightly. This helps when saving and loading a game.
        /// Warning Do not use a zero or short length.
        /// </summary>
        /// <param name="bodyA">The first body</param>
        /// <param name="bodyB">The second body</param>
        /// <param name="anchorA">The first body anchor</param>
        /// <param name="anchorB">The second body anchor</param>
        /// <param name="useWorldCoordinates">Set to true if you are using world coordinates as anchors.</param>
        public DistanceJoint(Body bodyA, Body bodyB, TSVector2 anchorA, TSVector2 anchorB, bool useWorldCoordinates = false)
            : base(bodyA, bodyB)
        {
            JointType = JointType.Distance;

            if (useWorldCoordinates)
            {
                LocalAnchorA = bodyA.GetLocalPoint(ref anchorA);
                LocalAnchorB = bodyB.GetLocalPoint(ref anchorB);
                Length = (anchorB - anchorA).magnitude;
            }
            else
            {
                LocalAnchorA = anchorA;
                LocalAnchorB = anchorB;
                Length = (BodyB.GetWorldPoint(ref anchorB) - BodyA.GetWorldPoint(ref anchorA)).magnitude;
            }
        }

        /// <summary>
        /// The local anchor point relative to bodyA's origin.
        /// </summary>
        public TSVector2 LocalAnchorA { get; set; }

        /// <summary>
        /// The local anchor point relative to bodyB's origin.
        /// </summary>
        public TSVector2 LocalAnchorB { get; set; }

        public override sealed TSVector2 WorldAnchorA
        {
            get { return BodyA.GetWorldPoint(LocalAnchorA); }
            set { Debug.Assert(false, "You can't set the world anchor on this joint type."); }
        }

        public override sealed TSVector2 WorldAnchorB
        {
            get { return BodyB.GetWorldPoint(LocalAnchorB); }
            set { Debug.Assert(false, "You can't set the world anchor on this joint type."); }
        }

        /// <summary>
        /// The natural length between the anchor points.
        /// Manipulating the length can lead to non-physical behavior when the frequency is zero.
        /// </summary>
        public FP Length { get; set; }

        /// <summary>
        /// The mass-spring-damper frequency in Hertz. A value of 0
        /// disables softness.
        /// </summary>
        public FP Frequency { get; set; }

        /// <summary>
        /// The damping ratio. 0 = no damping, 1 = critical damping.
        /// </summary>
        public FP DampingRatio { get; set; }

        /// <summary>
        /// Get the reaction force given the inverse time step. Unit is N.
        /// </summary>
        /// <param name="invDt"></param>
        /// <returns></returns>
        public override TSVector2 GetReactionForce(FP invDt)
        {
            TSVector2 F = (invDt * _impulse) * _u;
            return F;
        }

        /// <summary>
        /// Get the reaction torque given the inverse time step.
        /// Unit is N*m. This is always zero for a distance joint.
        /// </summary>
        /// <param name="invDt"></param>
        /// <returns></returns>
        public override FP GetReactionTorque(FP invDt)
        {
            return 0.0f;
        }

        internal override void InitVelocityConstraints(ref SolverData data)
        {
            _indexA = BodyA.IslandIndex;
            _indexB = BodyB.IslandIndex;
            _localCenterA = BodyA._sweep.LocalCenter;
            _localCenterB = BodyB._sweep.LocalCenter;
            _invMassA = BodyA._invMass;
            _invMassB = BodyB._invMass;
            _invIA = BodyA._invI;
            _invIB = BodyB._invI;

            TSVector2 cA = data.positions[_indexA].c;
            FP aA = data.positions[_indexA].a;
            TSVector2 vA = data.velocities[_indexA].v;
            FP wA = data.velocities[_indexA].w;

            TSVector2 cB = data.positions[_indexB].c;
            FP aB = data.positions[_indexB].a;
            TSVector2 vB = data.velocities[_indexB].v;
            FP wB = data.velocities[_indexB].w;

            Rot qA = new Rot(aA), qB = new Rot(aB);

            _rA = MathUtils.Mul(qA, LocalAnchorA - _localCenterA);
            _rB = MathUtils.Mul(qB, LocalAnchorB - _localCenterB);
            _u = cB + _rB - cA - _rA;

            // Handle singularity.
            FP length = _u.magnitude;
            if (length > Settings.LinearSlop)
            {
                _u *= 1.0f / length;
            }
            else
            {
                _u = TSVector2.zero;
            }

            FP crAu = MathUtils.Cross(_rA, _u);
            FP crBu = MathUtils.Cross(_rB, _u);
            FP invMass = _invMassA + _invIA * crAu * crAu + _invMassB + _invIB * crBu * crBu;

            // Compute the effective mass matrix.
            _mass = invMass != 0.0f ? 1.0f / invMass : 0.0f;

            if (Frequency > 0.0f)
            {
                FP C = length - Length;

                // Frequency
                FP omega = 2.0f * Settings.Pi * Frequency;

                // Damping coefficient
                FP d = 2.0f * _mass * DampingRatio * omega;

                // Spring stiffness
                FP k = _mass * omega * omega;

                // magic formulas
                FP h = data.step.dt;
                _gamma = h * (d + h * k);
                _gamma = _gamma != 0.0f ? 1.0f / _gamma : 0.0f;
                _bias = C * h * k * _gamma;

                invMass += _gamma;
                _mass = invMass != 0.0f ? 1.0f / invMass : 0.0f;
            }
            else
            {
                _gamma = 0.0f;
                _bias = 0.0f;
            }

            if (Settings.EnableWarmstarting)
            {
                // Scale the impulse to support a variable time step.
                _impulse *= data.step.dtRatio;

                TSVector2 P = _impulse * _u;
                vA -= _invMassA * P;
                wA -= _invIA * MathUtils.Cross(_rA, P);
                vB += _invMassB * P;
                wB += _invIB * MathUtils.Cross(_rB, P);
            }
            else
            {
                _impulse = 0.0f;
            }

            data.velocities[_indexA].v = vA;
            data.velocities[_indexA].w = wA;
            data.velocities[_indexB].v = vB;
            data.velocities[_indexB].w = wB;
        }

        internal override void SolveVelocityConstraints(ref SolverData data)
        {
            TSVector2 vA = data.velocities[_indexA].v;
            FP wA = data.velocities[_indexA].w;
            TSVector2 vB = data.velocities[_indexB].v;
            FP wB = data.velocities[_indexB].w;

            // Cdot = dot(u, v + cross(w, r))
            TSVector2 vpA = vA + MathUtils.Cross(wA, _rA);
            TSVector2 vpB = vB + MathUtils.Cross(wB, _rB);
            FP Cdot = TSVector2.Dot(_u, vpB - vpA);

            FP impulse = -_mass * (Cdot + _bias + _gamma * _impulse);
            _impulse += impulse;

            TSVector2 P = impulse * _u;
            vA -= _invMassA * P;
            wA -= _invIA * MathUtils.Cross(_rA, P);
            vB += _invMassB * P;
            wB += _invIB * MathUtils.Cross(_rB, P);

            data.velocities[_indexA].v = vA;
            data.velocities[_indexA].w = wA;
            data.velocities[_indexB].v = vB;
            data.velocities[_indexB].w = wB;

        }

        internal override bool SolvePositionConstraints(ref SolverData data)
        {
            if (Frequency > 0.0f)
            {
                // There is no position correction for soft distance constraints.
                return true;
            }

            TSVector2 cA = data.positions[_indexA].c;
            FP aA = data.positions[_indexA].a;
            TSVector2 cB = data.positions[_indexB].c;
            FP aB = data.positions[_indexB].a;

            Rot qA = new Rot(aA), qB = new Rot(aB);

            TSVector2 rA = MathUtils.Mul(qA, LocalAnchorA - _localCenterA);
            TSVector2 rB = MathUtils.Mul(qB, LocalAnchorB - _localCenterB);
            TSVector2 u = cB + rB - cA - rA;

            FP length = u.magnitude; u.Normalize();
            FP C = length - Length;
            C = MathUtils.Clamp(C, -Settings.MaxLinearCorrection, Settings.MaxLinearCorrection);

            FP impulse = -_mass * C;
            TSVector2 P = impulse * u;

            cA -= _invMassA * P;
            aA -= _invIA * MathUtils.Cross(rA, P);
            cB += _invMassB * P;
            aB += _invIB * MathUtils.Cross(rB, P);

            data.positions[_indexA].c = cA;
            data.positions[_indexA].a = aA;
            data.positions[_indexB].c = cB;
            data.positions[_indexB].a = aB;

            return FP.Abs(C) < Settings.LinearSlop;
        }
    }
}