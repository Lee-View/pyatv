# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class SendCommandResultMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    errorCode = ... # type: builtin___int
    handlerReturnStatus = ... # type: builtin___int
    handlerReturnStatusDatas = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes]

    def __init__(self,
        *,
        errorCode : typing___Optional[builtin___int] = None,
        handlerReturnStatus : typing___Optional[builtin___int] = None,
        handlerReturnStatusDatas : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> SendCommandResultMessage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"errorCode",u"handlerReturnStatus"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"errorCode",u"handlerReturnStatus",u"handlerReturnStatusDatas"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"errorCode",b"errorCode",u"handlerReturnStatus",b"handlerReturnStatus"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"errorCode",b"errorCode",u"handlerReturnStatus",b"handlerReturnStatus",u"handlerReturnStatusDatas",b"handlerReturnStatusDatas"]) -> None: ...

sendCommandResultMessage = ... # type: google___protobuf___descriptor___FieldDescriptor
