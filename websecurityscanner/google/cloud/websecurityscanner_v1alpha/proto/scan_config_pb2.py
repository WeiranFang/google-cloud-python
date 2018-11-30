# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1alpha/proto/scan_config.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1alpha/proto/scan_config.proto",
    package="google.cloud.websecurityscanner.v1alpha",
    syntax="proto3",
    serialized_pb=_b(
        '\n?google/cloud/websecurityscanner_v1alpha/proto/scan_config.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\x08\n\nScanConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x0f\n\x07max_qps\x18\x03 \x01(\x05\x12\x15\n\rstarting_urls\x18\x04 \x03(\t\x12Z\n\x0e\x61uthentication\x18\x05 \x01(\x0b\x32\x42.google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication\x12Q\n\nuser_agent\x18\x06 \x01(\x0e\x32=.google.cloud.websecurityscanner.v1alpha.ScanConfig.UserAgent\x12\x1a\n\x12\x62lacklist_patterns\x18\x07 \x03(\t\x12N\n\x08schedule\x18\x08 \x01(\x0b\x32<.google.cloud.websecurityscanner.v1alpha.ScanConfig.Schedule\x12\\\n\x10target_platforms\x18\t \x03(\x0e\x32\x42.google.cloud.websecurityscanner.v1alpha.ScanConfig.TargetPlatform\x1a\xf7\x02\n\x0e\x41uthentication\x12j\n\x0egoogle_account\x18\x01 \x01(\x0b\x32P.google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.GoogleAccountH\x00\x12j\n\x0e\x63ustom_account\x18\x02 \x01(\x0b\x32P.google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.CustomAccountH\x00\x1a\x33\n\rGoogleAccount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x1a\x46\n\rCustomAccount\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x11\n\tlogin_url\x18\x03 \x01(\tB\x10\n\x0e\x61uthentication\x1a]\n\x08Schedule\x12\x31\n\rschedule_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1e\n\x16interval_duration_days\x18\x02 \x01(\x05"`\n\tUserAgent\x12\x1a\n\x16USER_AGENT_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x43HROME_LINUX\x10\x01\x12\x12\n\x0e\x43HROME_ANDROID\x10\x02\x12\x11\n\rSAFARI_IPHONE\x10\x03"N\n\x0eTargetPlatform\x12\x1f\n\x1bTARGET_PLATFORM_UNSPECIFIED\x10\x00\x12\x0e\n\nAPP_ENGINE\x10\x01\x12\x0b\n\x07\x43OMPUTE\x10\x02\x42\x9b\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0fScanConfigProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_SCANCONFIG_USERAGENT = _descriptor.EnumDescriptor(
    name="UserAgent",
    full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.UserAgent",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="USER_AGENT_UNSPECIFIED", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CHROME_LINUX", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CHROME_ANDROID", index=2, number=2, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SAFARI_IPHONE", index=3, number=3, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=1112,
    serialized_end=1208,
)
_sym_db.RegisterEnumDescriptor(_SCANCONFIG_USERAGENT)

_SCANCONFIG_TARGETPLATFORM = _descriptor.EnumDescriptor(
    name="TargetPlatform",
    full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.TargetPlatform",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="TARGET_PLATFORM_UNSPECIFIED",
            index=0,
            number=0,
            options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="APP_ENGINE", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPUTE", index=2, number=2, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=1210,
    serialized_end=1288,
)
_sym_db.RegisterEnumDescriptor(_SCANCONFIG_TARGETPLATFORM)


_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT = _descriptor.Descriptor(
    name="GoogleAccount",
    full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.GoogleAccount",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="username",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.GoogleAccount.username",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.GoogleAccount.password",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=874,
    serialized_end=925,
)

_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT = _descriptor.Descriptor(
    name="CustomAccount",
    full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.CustomAccount",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="username",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.CustomAccount.username",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="password",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.CustomAccount.password",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="login_url",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.CustomAccount.login_url",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=927,
    serialized_end=997,
)

_SCANCONFIG_AUTHENTICATION = _descriptor.Descriptor(
    name="Authentication",
    full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="google_account",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.google_account",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="custom_account",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.custom_account",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT,
        _SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT,
    ],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="authentication",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.authentication",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=640,
    serialized_end=1015,
)

_SCANCONFIG_SCHEDULE = _descriptor.Descriptor(
    name="Schedule",
    full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Schedule",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="schedule_time",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Schedule.schedule_time",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="interval_duration_days",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.Schedule.interval_duration_days",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1017,
    serialized_end=1110,
)

_SCANCONFIG = _descriptor.Descriptor(
    name="ScanConfig",
    full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="max_qps",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.max_qps",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="starting_urls",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.starting_urls",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="authentication",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.authentication",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="user_agent",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.user_agent",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="blacklist_patterns",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.blacklist_patterns",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="schedule",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.schedule",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target_platforms",
            full_name="google.cloud.websecurityscanner.v1alpha.ScanConfig.target_platforms",
            index=8,
            number=9,
            type=14,
            cpp_type=8,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_SCANCONFIG_AUTHENTICATION, _SCANCONFIG_SCHEDULE],
    enum_types=[_SCANCONFIG_USERAGENT, _SCANCONFIG_TARGETPLATFORM],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=172,
    serialized_end=1288,
)

_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT.containing_type = _SCANCONFIG_AUTHENTICATION
_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT.containing_type = _SCANCONFIG_AUTHENTICATION
_SCANCONFIG_AUTHENTICATION.fields_by_name[
    "google_account"
].message_type = _SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT
_SCANCONFIG_AUTHENTICATION.fields_by_name[
    "custom_account"
].message_type = _SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT
_SCANCONFIG_AUTHENTICATION.containing_type = _SCANCONFIG
_SCANCONFIG_AUTHENTICATION.oneofs_by_name["authentication"].fields.append(
    _SCANCONFIG_AUTHENTICATION.fields_by_name["google_account"]
)
_SCANCONFIG_AUTHENTICATION.fields_by_name[
    "google_account"
].containing_oneof = _SCANCONFIG_AUTHENTICATION.oneofs_by_name["authentication"]
_SCANCONFIG_AUTHENTICATION.oneofs_by_name["authentication"].fields.append(
    _SCANCONFIG_AUTHENTICATION.fields_by_name["custom_account"]
)
_SCANCONFIG_AUTHENTICATION.fields_by_name[
    "custom_account"
].containing_oneof = _SCANCONFIG_AUTHENTICATION.oneofs_by_name["authentication"]
_SCANCONFIG_SCHEDULE.fields_by_name[
    "schedule_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCANCONFIG_SCHEDULE.containing_type = _SCANCONFIG
_SCANCONFIG.fields_by_name["authentication"].message_type = _SCANCONFIG_AUTHENTICATION
_SCANCONFIG.fields_by_name["user_agent"].enum_type = _SCANCONFIG_USERAGENT
_SCANCONFIG.fields_by_name["schedule"].message_type = _SCANCONFIG_SCHEDULE
_SCANCONFIG.fields_by_name["target_platforms"].enum_type = _SCANCONFIG_TARGETPLATFORM
_SCANCONFIG_USERAGENT.containing_type = _SCANCONFIG
_SCANCONFIG_TARGETPLATFORM.containing_type = _SCANCONFIG
DESCRIPTOR.message_types_by_name["ScanConfig"] = _SCANCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanConfig = _reflection.GeneratedProtocolMessageType(
    "ScanConfig",
    (_message.Message,),
    dict(
        Authentication=_reflection.GeneratedProtocolMessageType(
            "Authentication",
            (_message.Message,),
            dict(
                GoogleAccount=_reflection.GeneratedProtocolMessageType(
                    "GoogleAccount",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT,
                        __module__="google.cloud.websecurityscanner_v1alpha.proto.scan_config_pb2",
                        __doc__="""Describes authentication configuration that uses a Google account.
      
      
      Attributes:
          username:
              Required. The user name of the Google account.
          password:
              Input only. Required. The password of the Google account. The
              credential is stored encrypted and not returned in any
              response.
      """,
                        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.GoogleAccount)
                    ),
                ),
                CustomAccount=_reflection.GeneratedProtocolMessageType(
                    "CustomAccount",
                    (_message.Message,),
                    dict(
                        DESCRIPTOR=_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT,
                        __module__="google.cloud.websecurityscanner_v1alpha.proto.scan_config_pb2",
                        __doc__="""Describes authentication configuration that uses a custom account.
      
      
      Attributes:
          username:
              Required. The user name of the custom account.
          password:
              Input only. Required. The password of the custom account. The
              credential is stored encrypted and not returned in any
              response.
          login_url:
              Required. The login form URL of the website.
      """,
                        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication.CustomAccount)
                    ),
                ),
                DESCRIPTOR=_SCANCONFIG_AUTHENTICATION,
                __module__="google.cloud.websecurityscanner_v1alpha.proto.scan_config_pb2",
                __doc__="""Scan authentication configuration.
    
    
    Attributes:
        authentication:
            Required. Authentication configuration
        google_account:
            Authentication using a Google account.
        custom_account:
            Authentication using a custom account.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.ScanConfig.Authentication)
            ),
        ),
        Schedule=_reflection.GeneratedProtocolMessageType(
            "Schedule",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SCANCONFIG_SCHEDULE,
                __module__="google.cloud.websecurityscanner_v1alpha.proto.scan_config_pb2",
                __doc__="""Scan schedule configuration.
    
    
    Attributes:
        schedule_time:
            A timestamp indicates when the next run will be scheduled. The
            value is refreshed by the server after each run. If
            unspecified, it will default to current server time, which
            means the scan will be scheduled to start immediately.
        interval_duration_days:
            Required. The duration of time between executions in days.
    """,
                # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.ScanConfig.Schedule)
            ),
        ),
        DESCRIPTOR=_SCANCONFIG,
        __module__="google.cloud.websecurityscanner_v1alpha.proto.scan_config_pb2",
        __doc__="""A ScanConfig resource contains the configurations to launch a scan.
  
  
  Attributes:
      name:
          The resource name of the ScanConfig. The name follows the
          format of 'projects/{projectId}/scanConfigs/{scanConfigId}'.
          The ScanConfig IDs are generated by the system.
      display_name:
          Required. The user provided display name of the ScanConfig.
      max_qps:
          The maximum QPS during scanning. A valid value ranges from 5
          to 20 inclusively. If the field is unspecified or its value is
          set 0, server will default to 15. Other values outside of [5,
          20] range will be rejected with INVALID\_ARGUMENT error.
      starting_urls:
          Required. The starting URLs from which the scanner finds site
          pages.
      authentication:
          The authentication configuration. If specified, service will
          use the authentication configuration during scanning.
      user_agent:
          The user agent used during scanning.
      blacklist_patterns:
          The blacklist URL patterns as described in
          https://cloud.google.com/security-scanner/docs/excluded-urls
      schedule:
          The schedule of the ScanConfig.
      target_platforms:
          Set of Cloud Platforms targeted by the scan. If empty,
          APP\_ENGINE will be used as a default.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.ScanConfig)
    ),
)
_sym_db.RegisterMessage(ScanConfig)
_sym_db.RegisterMessage(ScanConfig.Authentication)
_sym_db.RegisterMessage(ScanConfig.Authentication.GoogleAccount)
_sym_db.RegisterMessage(ScanConfig.Authentication.CustomAccount)
_sym_db.RegisterMessage(ScanConfig.Schedule)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n+com.google.cloud.websecurityscanner.v1alphaB\017ScanConfigProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner"
    ),
)
# @@protoc_insertion_point(module_scope)
