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

        """Setup flat page generation.
        """
        pages.init_app(self.app)

        """Configure ability to freeze pages.
        """
        cube.init_app(self.app)

        """Load system modules
        """
        self.load_modules(app)

        if 'build' in environment:
            cube.freeze()

        logger.info('Application loading configuration from %s', _config)

    def load_modules(self, app):

        @app.route('/', methods=['GET'])
        def core_index_get():

            page = pages.get_or_404('index')

            template = page.meta.get('template', 'page.html')

            return render_template(template, page=page)

        @app.route('/<path:path>/', methods=['GET'])
        def core_page_get(path):

            page = pages.get_or_404(path)

            template = page.meta.get('template', 'page.html')

            return render_template(template, page=page)

        @cube.register_generator
        def core_page_get():
            for page in pages:
                yield {'path': page['path']}
