"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2015 gRPC authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class HelloRequest(google.protobuf.message.Message):
    """The request message containing the user's name and how many greetings
    they want.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    NUM_GREETINGS_FIELD_NUMBER: builtins.int
    name: builtins.str
    num_greetings: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        num_greetings: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "name", b"name", "num_greetings", b"num_greetings"
        ],
    ) -> None: ...

global___HelloRequest = HelloRequest

@typing_extensions.final
class HelloReply(google.protobuf.message.Message):
    """A response message containing a greeting"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_FIELD_NUMBER: builtins.int
    message: builtins.str
    def __init__(
        self,
        *,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["message", b"message"]
    ) -> None: ...

global___HelloReply = HelloReply
