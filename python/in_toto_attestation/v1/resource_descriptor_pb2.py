# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: in_toto_attestation/v1/resource_descriptor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0in_toto_attestation/v1/resource_descriptor.proto\x12\x16in_toto_attestation.v1\x1a\x1cgoogle/protobuf/struct.proto\"\x84\x03\n\x12ResourceDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x46\n\x06\x64igest\x18\x03 \x03(\x0b\x32\x36.in_toto_attestation.v1.ResourceDescriptor.DigestEntry\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\x0c\x12\x19\n\x11\x64ownload_location\x18\x05 \x01(\t\x12\x12\n\nmedia_type\x18\x06 \x01(\t\x12P\n\x0b\x61nnotations\x18\x07 \x03(\x0b\x32;.in_toto_attestation.v1.ResourceDescriptor.AnnotationsEntry\x1a-\n\x0b\x44igestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aJ\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\x42G\n\x1fio.github.intoto.attestation.v1Z$github.com/in-toto/attestation/go/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'in_toto_attestation.v1.resource_descriptor_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.github.intoto.attestation.v1Z$github.com/in-toto/attestation/go/v1'
  _RESOURCEDESCRIPTOR_DIGESTENTRY._options = None
  _RESOURCEDESCRIPTOR_DIGESTENTRY._serialized_options = b'8\001'
  _RESOURCEDESCRIPTOR_ANNOTATIONSENTRY._options = None
  _RESOURCEDESCRIPTOR_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _globals['_RESOURCEDESCRIPTOR']._serialized_start=107
  _globals['_RESOURCEDESCRIPTOR']._serialized_end=495
  _globals['_RESOURCEDESCRIPTOR_DIGESTENTRY']._serialized_start=374
  _globals['_RESOURCEDESCRIPTOR_DIGESTENTRY']._serialized_end=419
  _globals['_RESOURCEDESCRIPTOR_ANNOTATIONSENTRY']._serialized_start=421
  _globals['_RESOURCEDESCRIPTOR_ANNOTATIONSENTRY']._serialized_end=495
# @@protoc_insertion_point(module_scope)
