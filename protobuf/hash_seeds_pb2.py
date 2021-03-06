# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/hash-seeds.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/hash-seeds.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19protobuf/hash-seeds.proto\"<\n\x08HashSeed\x12\r\n\x05seed1\x18\x01 \x02(\x04\x12\r\n\x05seed2\x18\x02 \x02(\x04\x12\x12\n\nexpiryDate\x18\x03 \x02(\x04\"%\n\tHashSeeds\x12\x18\n\x05seeds\x18\x01 \x03(\x0b\x32\t.HashSeed'
)




_HASHSEED = _descriptor.Descriptor(
  name='HashSeed',
  full_name='HashSeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seed1', full_name='HashSeed.seed1', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seed2', full_name='HashSeed.seed2', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiryDate', full_name='HashSeed.expiryDate', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=89,
)


_HASHSEEDS = _descriptor.Descriptor(
  name='HashSeeds',
  full_name='HashSeeds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='seeds', full_name='HashSeeds.seeds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=128,
)

_HASHSEEDS.fields_by_name['seeds'].message_type = _HASHSEED
DESCRIPTOR.message_types_by_name['HashSeed'] = _HASHSEED
DESCRIPTOR.message_types_by_name['HashSeeds'] = _HASHSEEDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HashSeed = _reflection.GeneratedProtocolMessageType('HashSeed', (_message.Message,), {
  'DESCRIPTOR' : _HASHSEED,
  '__module__' : 'protobuf.hash_seeds_pb2'
  # @@protoc_insertion_point(class_scope:HashSeed)
  })
_sym_db.RegisterMessage(HashSeed)

HashSeeds = _reflection.GeneratedProtocolMessageType('HashSeeds', (_message.Message,), {
  'DESCRIPTOR' : _HASHSEEDS,
  '__module__' : 'protobuf.hash_seeds_pb2'
  # @@protoc_insertion_point(class_scope:HashSeeds)
  })
_sym_db.RegisterMessage(HashSeeds)


# @@protoc_insertion_point(module_scope)
