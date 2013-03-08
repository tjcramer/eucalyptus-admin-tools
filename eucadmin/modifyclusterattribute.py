# Copyright 2011-2012 Eucalyptus Systems, Inc.
#
# Redistribution and use of this software in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
#
#   Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from .adminservice import EucalyptusAdminRequest
from requestbuilder import Arg
import argparse
import sys

class EncodeProperty(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        t = value.split('=')
        if len(t) != 2:
            print >>sys.stderr "Options must be of the form KEY=VALUE: %s" % value
            sys.exit(1)
        setattr(namespace, 'Attribute', t[0])
        setattr(namespace, 'Value', t[1])

class ModifyClusterAttribute(EucalyptusAdminRequest):
    SERVICE_PATH = 'services/Properties'
    DESCRIPTION = 'Modify cluster attribute'

    ARGS = [ Arg('Name', '--name',
                 help='The cluster name')]
             Arg('-p', '--property', dest='property',
                required=True,
                action=EncodeProperty,
                help='Modify attribute (KEY=VALUE)'),
             Arg('-P', '--partition', dest='Partition',
                 help='Partition for the cluster.')]

    def process_cli_args(self):
        EucalyptusAdminRequest.process_cli_args(self)
        for key in ['Attribute', 'Value']:
            self._arg_routes[key] = self.params

    def print_result(self, data):
        print data
