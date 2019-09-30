# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class NowPlayingClient(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    processIdentifier = ... # type: int
    bundleIdentifier = ... # type: typing___Text
    parentApplicationBundleIdentifier = ... # type: typing___Text
    processUserIdentifier = ... # type: int
    nowPlayingVisibility = ... # type: int
    displayName = ... # type: typing___Text

    def __init__(self,
        *,
        processIdentifier : typing___Optional[int] = None,
        bundleIdentifier : typing___Optional[typing___Text] = None,
        parentApplicationBundleIdentifier : typing___Optional[typing___Text] = None,
        processUserIdentifier : typing___Optional[int] = None,
        nowPlayingVisibility : typing___Optional[int] = None,
        displayName : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> NowPlayingClient: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"bundleIdentifier",u"displayName",u"nowPlayingVisibility",u"parentApplicationBundleIdentifier",u"processIdentifier",u"processUserIdentifier"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"bundleIdentifier",u"displayName",u"nowPlayingVisibility",u"parentApplicationBundleIdentifier",u"processIdentifier",u"processUserIdentifier"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"bundleIdentifier",b"bundleIdentifier",u"displayName",b"displayName",u"nowPlayingVisibility",b"nowPlayingVisibility",u"parentApplicationBundleIdentifier",b"parentApplicationBundleIdentifier",u"processIdentifier",b"processIdentifier",u"processUserIdentifier",b"processUserIdentifier"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"bundleIdentifier",b"bundleIdentifier",u"displayName",b"displayName",u"nowPlayingVisibility",b"nowPlayingVisibility",u"parentApplicationBundleIdentifier",b"parentApplicationBundleIdentifier",u"processIdentifier",b"processIdentifier",u"processUserIdentifier",b"processUserIdentifier"]) -> None: ...