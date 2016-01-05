"""

  start.py
  StaticVI::Core

  Created by Viable Industries, L.L.C. on 01/05/2016.
  Copyright (c) 2011-2016 Viable Industries, L.L.C. All rights reserved.

"""


import os
import sys
import itertools
import logging

from flask import Flask
from flask import render_template

from flask_frozen import Freezer
from flask.ext.flatpages import FlatPages


"""
Define our application variable
"""
commonscloudstatic = Flask(__name__, template_folder='_templates')

"""
Load our configuration
"""
commonscloudstatic.config.from_object('constants')


pages = FlatPages(commonscloudstatic)
cube = Freezer(commonscloudstatic)


"""
Front page
"""
@commonscloudstatic.route('/')
def index():
    page = pages.get_or_404('index')
    return render_template('index.html', page=page, pages=pages)


"""
Other pages
"""
@commonscloudstatic.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    template = page.meta.get('template', 'page.html')
    return render_template(template, page=page, pages=pages);


"""
URL Generator for pages
"""
@cube.register_generator
def page():
    for page in pages:
      yield {'path': page['permalink']}

"""
Check to ensure that the application is loaded through
a virtual enviornment. If it is not, prompt the user
to either install a virtual enviornment or activate
the one with the applciation.
"""
if __name__ == "__main__":
    if "VIRTUAL_ENV" not in os.environ:
        print("""
        Your Virtual Environment or virtualenv has not been activated.

        To use this application, please activate it by executing:

          source venv/bin/activate

        If the problem persists, ensure that virtualenv is installed:

          pip install virtualenv

        and that all other requirements have been satisfied.
        """)
    elif len(sys.argv) > 1 and sys.argv[1] == "build":
        cube.freeze()
    else:
        commonscloudstatic.run(port=commonscloudstatic.config['PORT'])
