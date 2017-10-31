#!/usr/bin/env python

"""User module views.

Created by Viable Industries, L.L.C. on 12/27/2015.
Copyright 2016 Viable Industries, L.L.C. All rights reserved.

For license and copyright information please see the LICENSE document (the
"License") included with this software package. This file may not be used
in any manner except in compliance with the License unless required by
applicable law or agreed to in writing, software distributed under the
License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and
limitations under the License.
"""


from . import module


from flask import render_template


from app import pages


@module.route('/', methods=['GET'])
def core_index_get():

    page = pages.get_or_404('index')

    template = page.meta.get('template', 'page.html')

    return render_template(template, page=page)


@module.route('/<path:path>/', methods=['GET'])
def core_page_get(path):

    page = pages.get_or_404(path)

    template = page.meta.get('template', 'page.html')

    return render_template(template, page=page)
