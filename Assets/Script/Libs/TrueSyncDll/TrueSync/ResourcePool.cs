using System;
using System.Collections.Generic;

namespace TrueSync
{
    /// <summary>
    /// DV 资源池(抽象类)
    /// 是一个抽象对象池,他有一个静态对象池列表。他管理所有对象池的清理CleanUpAll();
    /// </summary>
	public abstract class ResourcePool
	{
		protected bool fresh = true;

        // 为了清空所有资源池而存在
		protected static List<ResourcePool> resourcePoolReferences = new List<ResourcePool>();

        // 全部清空
		public static void CleanUpAll()
		{
			int i = 0;
			int count = ResourcePool.resourcePoolReferences.Count;
			while (i < count)
			{
				ResourcePool.resourcePoolReferences[i].ResetResourcePool();
				i++;
			}
			ResourcePool.resourcePoolReferences.Clear();
		}

        // 重置
		public abstract void ResetResourcePool();
	}

    // 资源池
	public class ResourcePool<T> : ResourcePool
	{
		protected Stack<T> stack = new Stack<T>(10);

        #region 公共方法
        // 池中元素的数量
		public int Count
		{
			get
			{
				return this.stack.Count;
			}
		}

        // 重置
		public override void ResetResourcePool()
		{
			this.stack.Clear();
			this.fresh = true;
		}

        /// <summary>
        /// 回收元素
        /// DV 还回对象
        /// </summary>
		public void GiveBack(T obj)
		{
			this.stack.Push(obj);
		}

        /// <summary>
        /// 获取元素
        /// DV 获取对象, 如果T是ResourcePoolItem的派生类就会调对象的CleanUp()方法
        /// </summary>
        public T GetNew()
        {
            bool fresh = this.fresh;
            if (fresh)
            {
                ResourcePool.resourcePoolReferences.Add(this);
                this.fresh = false;
            }
            bool flag = this.stack.Count == 0;
            if (flag) // 池中没有元素
            {
                this.stack.Push(this.NewInstance());
            }
            T t = this.stack.Pop();
            bool flag2 = t is ResourcePoolItem;
            if (flag2) // 如果该元素是ResourcePoolItem类型，则要先执行清理
            {
                ((ResourcePoolItem)((object)t)).CleanUp();
            }
            return t;
        }
        #endregion 公共方法

        /// <summary>
        /// 创建元素实例:实例化对象
        /// </summary>
		protected virtual T NewInstance()
		{
			return Activator.CreateInstance<T>();
		}
	}
}
