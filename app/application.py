#!/usr/bin/env python

"""Copyright and License Information.

Create by Viable Industries, L.L.C. on 05/16/2017.
Copyright 2016 Viable Industries, L.L.C. All rights reserved.

For license and copyright information please see the LICENSE.md (the "License")
document packaged with this software. This file and all other files included in
this packaged software may not be used in any manner except in compliance with
the License. Software distributed under this License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTY, OR CONDITIONS OF ANY KIND, either express or
implied.

See the License for the specific language governing permission and limitations
under the License.
"""


import imp
import os


from datetime import datetime


from . import cube
from . import flask
from . import logger
from . import pages


from flask import render_template


class Application(object):
    """Create Flask Application via a Class."""

    def __init__(self, environment, name, app=None, extensions={}):
        """Application Constructor.

        Setup our base Flask application, retaining it as our application
        object for use throughout the application

        :param (class) self
            The representation of the instantiated Class Instance
        :param (str) name
            The name of the application
        :param (str) environment
            The name of the enviornment in which to load the application
        :param (class) app
            The Flask class for the application that was created
        """
        logger.info('Application Started at %s', datetime.utcnow())

        self.name = name
        self.environment = environment
        self.extensions = extensions

        """Create our base Flask application
        """
        app = flask.Flask(__name__, static_path='/static')
        self.app = app
        logger.info('Starting application named `%s`' % __name__)

        """Import all custom app configurations
        """
        _config = ('config/%s.config') % (environment)

        """Read the JSON configuration file content.
        """
        self.app.config.from_json(_config)

        pages.init_app(self.app)

        """Load system modules
        """
        self.load_modules()

        logger.info('Application loading configuration from %s', _config)

    def load_modules(self):
        """Load all application modules.

        Open the module path defined in the configuration, for each module
        directory found in the defined module path we need to `load_module`,
        and create a Flask Blueprint with the module information.

        :param (object) self
            the current class (i.e., Application)
        """
        logger.info('Application beginning to load modules')

        modules_path = self.app.config['MODULE_PATH']
        modules_directory = os.listdir(modules_path)

        modules_list = {}

        for module_name in modules_directory:

            module_path = os.path.join(modules_path, module_name)
            module_package = os.path.join(modules_path, module_name,
                                          '__init__.py')

            if os.path.isdir(module_path):

                """Locate and load the module into our module_list
                """
                try:
                    f, filename, descr = imp.find_module(module_name,
                                                         [modules_path])
                    modules_list[module_name] = imp.load_module(module_name,
                                                                f, filename,
                                                                descr)
                except ImportError:
                    logger.error('`load_modules` was unable to locate the'
                                 '`__init__.py` file in your %s module' %
                                 (module_name))
                    raise

                """Register this module with the application as a blueprint

                See the official Flask API for more information about Blueprint
                http://flask.pocoo.org/docs/0.10/api/#flask.Flask.register_blueprint
                """
                if hasattr(modules_list[module_name], 'module'):
                    module_blueprint = modules_list[module_name].module
                    self.app.register_blueprint(module_blueprint)

                    logger.info('Application successfully loaded `%s` module' %
                                (module_name))

                else:
                    logger.error('Application failed to load `%s` module' %
                                 (module_name))
