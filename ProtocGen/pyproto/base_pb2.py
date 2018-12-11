# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base.proto',
  package='Google.Protobuf',
  syntax='proto3',
  serialized_pb=_b('\n\nbase.proto\x12\x0fGoogle.Protobuf\"D\n\x0bGameMessage\x12\'\n\x04Type\x18\x01 \x01(\x0e\x32\x19.Google.Protobuf.Protocol\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\x0c\"-\n\x08ReqLogin\x12\x0f\n\x07\x41\x63\x63ount\x18\x01 \x01(\t\x12\x10\n\x08Password\x18\x02 \x01(\t\"=\n\x08\x41\x63kLogin\x12\x0f\n\x07Success\x18\x01 \x01(\r\x12\x0e\n\x06Userid\x18\x02 \x01(\r\x12\x10\n\x08Nickname\x18\x03 \x01(\t\"-\n\x08ReqMatch\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x11\n\tFightType\x18\x02 \x01(\r\".\n\nPlayerInfo\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x10\n\x08Nickname\x18\x02 \x01(\t\"O\n\x08NtfMatch\x12\x33\n\x0ePlayerinfoList\x18\x01 \x03(\x0b\x32\x1b.Google.Protobuf.PlayerInfo\x12\x0e\n\x06Roomid\x18\x02 \x01(\r\"?\n\rReqSelectHero\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x0e\n\x06Roomid\x18\x02 \x01(\r\x12\x0e\n\x06Heroid\x18\x03 \x01(\r\"0\n\x0ePlayerHeroInfo\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x0e\n\x06Heroid\x18\x02 \x01(\r\"N\n\x13NtfSelectHeroFinish\x12\x37\n\x0eSelectHerolist\x18\x01 \x03(\x0b\x32\x1f.Google.Protobuf.PlayerHeroInfo\".\n\x0cReqGameStart\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x0e\n\x06Roomid\x18\x02 \x01(\r\".\n\x0cReqStartMove\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x0e\n\x06Roomid\x18\x02 \x01(\r\"=\n\x0cReqChangeDir\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x0e\n\x06Roomid\x18\x02 \x01(\r\x12\r\n\x05\x41ngle\x18\x03 \x01(\x05\",\n\nReqEndMove\x12\x0e\n\x06Userid\x18\x01 \x01(\r\x12\x0e\n\x06Roomid\x18\x02 \x01(\r*\xde\x02\n\x08Protocol\x12\x18\n\x14Protocol_GameMessage\x10\x00\x12\x15\n\x11Protocol_ReqLogin\x10\x01\x12\x15\n\x11Protocol_AckLogin\x10\x02\x12\x15\n\x11Protocol_ReqMatch\x10\x03\x12\x17\n\x13Protocol_PlayerInfo\x10\x04\x12\x15\n\x11Protocol_NtfMatch\x10\x05\x12\x1a\n\x16Protocol_ReqSelectHero\x10\x06\x12\x1b\n\x17Protocol_PlayerHeroInfo\x10\x07\x12 \n\x1cProtocol_NtfSelectHeroFinish\x10\x08\x12\x19\n\x15Protocol_ReqGameStart\x10\t\x12\x19\n\x15Protocol_ReqStartMove\x10\n\x12\x19\n\x15Protocol_ReqChangeDir\x10\x0b\x12\x17\n\x13Protocol_ReqEndMove\x10\x0c\x62\x06proto3')
)

_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='Google.Protobuf.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Protocol_GameMessage', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_ReqLogin', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_AckLogin', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_ReqMatch', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_PlayerInfo', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_NtfMatch', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_ReqSelectHero', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_PlayerHeroInfo', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_NtfSelectHeroFinish', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_ReqGameStart', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_ReqStartMove', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_ReqChangeDir', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Protocol_ReqEndMove', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=788,
  serialized_end=1138,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOL)

Protocol = enum_type_wrapper.EnumTypeWrapper(_PROTOCOL)
Protocol_GameMessage = 0
Protocol_ReqLogin = 1
Protocol_AckLogin = 2
Protocol_ReqMatch = 3
Protocol_PlayerInfo = 4
Protocol_NtfMatch = 5
Protocol_ReqSelectHero = 6
Protocol_PlayerHeroInfo = 7
Protocol_NtfSelectHeroFinish = 8
Protocol_ReqGameStart = 9
Protocol_ReqStartMove = 10
Protocol_ReqChangeDir = 11
Protocol_ReqEndMove = 12



_GAMEMESSAGE = _descriptor.Descriptor(
  name='GameMessage',
  full_name='Google.Protobuf.GameMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='Google.Protobuf.GameMessage.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Data', full_name='Google.Protobuf.GameMessage.Data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=99,
)


_REQLOGIN = _descriptor.Descriptor(
  name='ReqLogin',
  full_name='Google.Protobuf.ReqLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Account', full_name='Google.Protobuf.ReqLogin.Account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Password', full_name='Google.Protobuf.ReqLogin.Password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=146,
)


_ACKLOGIN = _descriptor.Descriptor(
  name='AckLogin',
  full_name='Google.Protobuf.AckLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Success', full_name='Google.Protobuf.AckLogin.Success', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.AckLogin.Userid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Nickname', full_name='Google.Protobuf.AckLogin.Nickname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=209,
)


_REQMATCH = _descriptor.Descriptor(
  name='ReqMatch',
  full_name='Google.Protobuf.ReqMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.ReqMatch.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FightType', full_name='Google.Protobuf.ReqMatch.FightType', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=256,
)


_PLAYERINFO = _descriptor.Descriptor(
  name='PlayerInfo',
  full_name='Google.Protobuf.PlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.PlayerInfo.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Nickname', full_name='Google.Protobuf.PlayerInfo.Nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=304,
)


_NTFMATCH = _descriptor.Descriptor(
  name='NtfMatch',
  full_name='Google.Protobuf.NtfMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PlayerinfoList', full_name='Google.Protobuf.NtfMatch.PlayerinfoList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Roomid', full_name='Google.Protobuf.NtfMatch.Roomid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=385,
)


_REQSELECTHERO = _descriptor.Descriptor(
  name='ReqSelectHero',
  full_name='Google.Protobuf.ReqSelectHero',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.ReqSelectHero.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Roomid', full_name='Google.Protobuf.ReqSelectHero.Roomid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Heroid', full_name='Google.Protobuf.ReqSelectHero.Heroid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=387,
  serialized_end=450,
)


_PLAYERHEROINFO = _descriptor.Descriptor(
  name='PlayerHeroInfo',
  full_name='Google.Protobuf.PlayerHeroInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.PlayerHeroInfo.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Heroid', full_name='Google.Protobuf.PlayerHeroInfo.Heroid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=500,
)


_NTFSELECTHEROFINISH = _descriptor.Descriptor(
  name='NtfSelectHeroFinish',
  full_name='Google.Protobuf.NtfSelectHeroFinish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SelectHerolist', full_name='Google.Protobuf.NtfSelectHeroFinish.SelectHerolist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=580,
)


_REQGAMESTART = _descriptor.Descriptor(
  name='ReqGameStart',
  full_name='Google.Protobuf.ReqGameStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.ReqGameStart.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Roomid', full_name='Google.Protobuf.ReqGameStart.Roomid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=628,
)


_REQSTARTMOVE = _descriptor.Descriptor(
  name='ReqStartMove',
  full_name='Google.Protobuf.ReqStartMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.ReqStartMove.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Roomid', full_name='Google.Protobuf.ReqStartMove.Roomid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=676,
)


_REQCHANGEDIR = _descriptor.Descriptor(
  name='ReqChangeDir',
  full_name='Google.Protobuf.ReqChangeDir',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.ReqChangeDir.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Roomid', full_name='Google.Protobuf.ReqChangeDir.Roomid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Angle', full_name='Google.Protobuf.ReqChangeDir.Angle', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=678,
  serialized_end=739,
)


_REQENDMOVE = _descriptor.Descriptor(
  name='ReqEndMove',
  full_name='Google.Protobuf.ReqEndMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Userid', full_name='Google.Protobuf.ReqEndMove.Userid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Roomid', full_name='Google.Protobuf.ReqEndMove.Roomid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=785,
)

_GAMEMESSAGE.fields_by_name['Type'].enum_type = _PROTOCOL
_NTFMATCH.fields_by_name['PlayerinfoList'].message_type = _PLAYERINFO
_NTFSELECTHEROFINISH.fields_by_name['SelectHerolist'].message_type = _PLAYERHEROINFO
DESCRIPTOR.message_types_by_name['GameMessage'] = _GAMEMESSAGE
DESCRIPTOR.message_types_by_name['ReqLogin'] = _REQLOGIN
DESCRIPTOR.message_types_by_name['AckLogin'] = _ACKLOGIN
DESCRIPTOR.message_types_by_name['ReqMatch'] = _REQMATCH
DESCRIPTOR.message_types_by_name['PlayerInfo'] = _PLAYERINFO
DESCRIPTOR.message_types_by_name['NtfMatch'] = _NTFMATCH
DESCRIPTOR.message_types_by_name['ReqSelectHero'] = _REQSELECTHERO
DESCRIPTOR.message_types_by_name['PlayerHeroInfo'] = _PLAYERHEROINFO
DESCRIPTOR.message_types_by_name['NtfSelectHeroFinish'] = _NTFSELECTHEROFINISH
DESCRIPTOR.message_types_by_name['ReqGameStart'] = _REQGAMESTART
DESCRIPTOR.message_types_by_name['ReqStartMove'] = _REQSTARTMOVE
DESCRIPTOR.message_types_by_name['ReqChangeDir'] = _REQCHANGEDIR
DESCRIPTOR.message_types_by_name['ReqEndMove'] = _REQENDMOVE
DESCRIPTOR.enum_types_by_name['Protocol'] = _PROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameMessage = _reflection.GeneratedProtocolMessageType('GameMessage', (_message.Message,), dict(
  DESCRIPTOR = _GAMEMESSAGE,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.GameMessage)
  ))
_sym_db.RegisterMessage(GameMessage)

ReqLogin = _reflection.GeneratedProtocolMessageType('ReqLogin', (_message.Message,), dict(
  DESCRIPTOR = _REQLOGIN,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.ReqLogin)
  ))
_sym_db.RegisterMessage(ReqLogin)

AckLogin = _reflection.GeneratedProtocolMessageType('AckLogin', (_message.Message,), dict(
  DESCRIPTOR = _ACKLOGIN,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.AckLogin)
  ))
_sym_db.RegisterMessage(AckLogin)

ReqMatch = _reflection.GeneratedProtocolMessageType('ReqMatch', (_message.Message,), dict(
  DESCRIPTOR = _REQMATCH,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.ReqMatch)
  ))
_sym_db.RegisterMessage(ReqMatch)

PlayerInfo = _reflection.GeneratedProtocolMessageType('PlayerInfo', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERINFO,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.PlayerInfo)
  ))
_sym_db.RegisterMessage(PlayerInfo)

NtfMatch = _reflection.GeneratedProtocolMessageType('NtfMatch', (_message.Message,), dict(
  DESCRIPTOR = _NTFMATCH,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.NtfMatch)
  ))
_sym_db.RegisterMessage(NtfMatch)

ReqSelectHero = _reflection.GeneratedProtocolMessageType('ReqSelectHero', (_message.Message,), dict(
  DESCRIPTOR = _REQSELECTHERO,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.ReqSelectHero)
  ))
_sym_db.RegisterMessage(ReqSelectHero)

PlayerHeroInfo = _reflection.GeneratedProtocolMessageType('PlayerHeroInfo', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERHEROINFO,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.PlayerHeroInfo)
  ))
_sym_db.RegisterMessage(PlayerHeroInfo)

NtfSelectHeroFinish = _reflection.GeneratedProtocolMessageType('NtfSelectHeroFinish', (_message.Message,), dict(
  DESCRIPTOR = _NTFSELECTHEROFINISH,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.NtfSelectHeroFinish)
  ))
_sym_db.RegisterMessage(NtfSelectHeroFinish)

ReqGameStart = _reflection.GeneratedProtocolMessageType('ReqGameStart', (_message.Message,), dict(
  DESCRIPTOR = _REQGAMESTART,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.ReqGameStart)
  ))
_sym_db.RegisterMessage(ReqGameStart)

ReqStartMove = _reflection.GeneratedProtocolMessageType('ReqStartMove', (_message.Message,), dict(
  DESCRIPTOR = _REQSTARTMOVE,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.ReqStartMove)
  ))
_sym_db.RegisterMessage(ReqStartMove)

ReqChangeDir = _reflection.GeneratedProtocolMessageType('ReqChangeDir', (_message.Message,), dict(
  DESCRIPTOR = _REQCHANGEDIR,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.ReqChangeDir)
  ))
_sym_db.RegisterMessage(ReqChangeDir)

ReqEndMove = _reflection.GeneratedProtocolMessageType('ReqEndMove', (_message.Message,), dict(
  DESCRIPTOR = _REQENDMOVE,
  __module__ = 'base_pb2'
  # @@protoc_insertion_point(class_scope:Google.Protobuf.ReqEndMove)
  ))
_sym_db.RegisterMessage(ReqEndMove)


# @@protoc_insertion_point(module_scope)