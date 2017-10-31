#!/usr/bin/env python

"""Viable Data.

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


import argparse
import logging
import flask


from flask_frozen import Freezer
from flask_flatpages import FlatPages


"""System Logging.

System logging enables us to retain useful activity within the system in
server logs. Log messages are written to the Terminal or Application Runner
(e.g., Supervisor) server logs.

Below sets up the `basicConfig` which opens a stream that allows us to add
formatted log messages to the root logger.

@param (object) logger
    Provides the ability to write directly to the logger with the info(),
    warning(), error(), and critical() methods

See the official Python::logging documentation for more Information
https://docs.python.org/2/library/logging.html
"""
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


"""Compile Markdown files and HTML files into a static site.

Flask-FlatPages provides a collection of pages to your Flask application. Pages
are built from "flat" text files as opposed to a relational database.

See the official FlatPages documentation for more information on usage
http://flask-flatpages.readthedocs.io/en/latest/
"""
pages = FlatPages()


"""Freezer takes our "FlatPages" from above and generates a full static site.

Frozen-Flask freezes a Flask application into a set of static files. The result
can be hosted without any server-side software other than a traditional web
server.

See the official Freezer documentation for more information on usage
http://pythonhosted.org/Frozen-Flask/
"""
cube = Freezer()


"""Meta Information.
"""
__author__ = 'Joshua I. Powell'
__copyright__ = 'Copyright 2017 Viable Industries, L.L.C. All rights reserved.'
__date__ = '2017-10-30'
__license__ = 'MIT'
__organization__ = 'Viable Industries, L.L.C.'
__status__ = 'Production'
__version__ = '2.0.0'
