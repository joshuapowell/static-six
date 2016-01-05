"""

    application_arguments.py
    FieldStack::ApplicationArguments

    Created by Viable Industries, L.L.C. on 12/27/2015.
    Copyright (c) 2015 Viable Industries, L.L.C. All rights reserved.

    For license and copyright information please see the LICENSE document (the
    "License") included with this software package. This file may not be used
    in any manner except in compliance with the License unless required by
    applicable law or agreed to in writing, software distributed under the
    License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
    CONDITIONS OF ANY KIND, either express or implied.

    See the License for the specific language governing permissions and
    limitations under the License.

"""


from . import argparse


class Arguments(object):

    """
    Application Arguments Constructor

    Setup named application arguments and command line interface help
    information.

    @param (class) self
        The representation of the instantiated Class Instance
    @param (class) parser
        The name of the application
    @param (class) args
        The name of the enviornment in which to load the application
    """
    def __init__(self, parser=None, args=None):

        self.parser = argparse.ArgumentParser(**{
            'prog': 'FieldStack',
            'description': 'The FieldStack Core API service'
        })

        self.parser.add_argument('--environment', **{
            'type': str,
            'help': 'set application environment (default: testing)',
            'default': 'testing'
        })

        self.parser.add_argument('--host', **{
            'type': str,
            'help': 'set hostname to listen on (default: 127.0.0.1)',
            'default': '127.0.0.1'
        })

        self.parser.add_argument('--port', **{
            'type': int,
            'help': 'set port of webserver (default: 5000)',
            'default': 5000
        })

        self.parser.add_argument('--debug', **{
            'type': bool,
            'help': 'enable or disable debug mode (default: False)',
            'default': False
        })

        self.args = self.parser.parse_args()
