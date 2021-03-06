# Copyright 2013 IBM Corporation
# Copyright 2015-2017 Lenovo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# The Exceptions that Pyghmi can throw


class PyghmiException(Exception):
    pass


class IpmiException(PyghmiException):
    def __init__(self, text='', code=0):
        super(IpmiException, self).__init__(text)
        self.ipmicode = code


class RedfishError(PyghmiException):
    def __init__(self, text='', msgid=None):
        super(RedfishError, self).__init__(text)
        self.msgid = msgid


class UnrecognizedCertificate(Exception):
    def __init__(self, text='', certdata=None):
        super(UnrecognizedCertificate, self).__init__(text)
        self.certdata = certdata


class TemporaryError(Exception):
    # A temporary condition that should clear, but warrants reporting to the
    # caller
    pass


class InvalidParameterValue(PyghmiException):
    pass


class BmcErrorException(IpmiException):
    # This denotes when library detects an invalid BMC behavior
    pass


class UnsupportedFunctionality(PyghmiException):
    # Indicates when functionality is requested that is not supported by
    # current endpoint
    pass


class BypassGenericBehavior(PyghmiException):
    # Indicates that an OEM handler wants to abort any standards based
    # follow up
    pass


class FallbackData(PyghmiException):
    # Indicates the OEM handler has data to be used if the generic
    # check comes up empty
    def __init__(self, fallbackdata):
        self.fallbackdata = fallbackdata

    pass
