"""

    application.py
    StaticVI::Application

    Created by Viable Industries, L.L.C. on 01/05/2016.
    Copyright (c) 2011-2016 Viable Industries, L.L.C. All rights reserved.

    For license and copyright information please see the LICENSE document (the
    "License") included with this software package. This file may not be used
    in any manner except in compliance with the License unless required by
    applicable law or agreed to in writing, software distributed under the
    License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
    CONDITIONS OF ANY KIND, either express or implied.

    See the License for the specific language governing permissions and
    limitations under the License.

"""


from . import flask


class Application(object):

    """Application Constructor

    Setup our base Flask application, retaining it as our application
    object for use throughout the application

    @param (class) self
        The representation of the instantiated Class Instance
    @param (str) name
        The name of the application
    @param (str) environment
        The name of the enviornment in which to load the application
    @param (class) app
        The Flask class for the application that was created
    """
    def __init__(self, environment, name, app=None, extensions={}):

        self.name = name
        self.environment = environment
        self.extensions = extensions

        self.app = flask.Flask(__name__, **{
            'static_path': '/static',
            'template_folder': '_templates'
        })

        self.app.config.from_object(('src.config.%s') % (environment))
