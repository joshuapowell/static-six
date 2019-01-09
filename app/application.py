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
        app = flask.Flask(__name__, static_url_path='/static')
        self.app = app
        logger.info('Starting StaticVI')

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
        self.generate_pages(app)

        """Freeze all files if this is the build environment.
        """
        if 'build' in environment:
            cube.freeze()

        logger.info('StaticVI completed loading')

    def generate_pages(self, app):
        """Generate site pages.

        Create an index and other pages from the `pages` directory.

        :param (class) self
            The representation of the instantiated Class Instance
        :param (str) app
            The application object to attach the routes to
        """
        logger.info('StaticVI generating static index and user-named pages')

        @app.route('/', methods=['GET'])
        def core_index_get():
            """Index page.

            :return (object) render_template
                A dynamically rendered HTML page.
            """

            page = pages.get_or_404('index')

            template = page.meta.get('template', 'page.html')

            return render_template(template, page=page)

        @app.route('/<path:path>/', methods=['GET'])
        def core_page_get(path):
            """Dynamically routed (you-name-it) pages.

            :return (object) render_template
                A dynamically rendered HTML page.
            """

            page = pages.get_or_404(path)

            template = page.meta.get('template', 'page.html')

            return render_template(template, page=page)

        @cube.register_generator
        def core_page_get():
            """URL Generator.

            Freeze pages from these routes when building static pages to the
            static `build` directory.

            See official Frozen Flask documentation for more information.
            http://pythonhosted.org/Frozen-Flask/#url-generators
            """
            for page in pages:
                logger.info('StaticVI creating static page for %s',
                            page['path'])
                yield {'path': page['path']}
