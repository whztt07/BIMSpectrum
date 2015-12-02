# **************************************************************************
# *
# Copyright (c) 2015 * 
# Ling Ma <bitly.com/cvlingma> * 
# *
# This program is free software; you can redistribute it and/or modify *
# it under the terms of the GNU Lesser General Public License (LGPL) *
# as published by the Free Software Foundation; either version 2 of *
# the License, or (at your option) any later version. *
# for detail see the LICENCE text file. *
# *
# This program is distributed in the hope that it will be useful, *
# but WITHOUT ANY WARRANTY; without even the implied warranty of *
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the *
# GNU Library General Public License for more details. *
# *
# You should have received a copy of the GNU Library General Public *
# License along with this program; if not, write to the Free Software *
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 *
# USA *
# *
# **************************************************************************

__author__ = 'ling'

from flask import Blueprint, render_template
from project import app
import requests
import json

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


# use decorators to link the function to a url
@home_blueprint.route('/')
# @login_required # pragma: no cover 
def home():
    if app.config['TESTING']:
        user_id = "abcdef"
        username = "Ling"
        email = "malingreal@gmail.com"
    else:
        user_id = "abcdef"
        username = "Ling"
        email = "malingreal@gmail.com"
        # username = user.given_name
        # email = user.email
        # user_id = user.get_id()[-22:]
    description = "test"

    # #TODO this version we assume each user has only one project
    project_id = ""
    r = requests.get(app.config['API_URL'] + "/project?user_id=" + user_id)
    project_items = r.json()
    if len(project_items['_items']) == 0:
        r = requests.post(app.config['API_URL'] + "/project",
                          data={"username": username, "email": email, "user_id": user_id, "description": description})
        project_items = r.json()
        project_id = project_items["_id"]
    else:
        project_info = project_items['_items'][0]
        project_id = project_info['_id']
    r = requests.get(app.config['API_URL'] + "/file?project_id=" + project_id)
    # return json.dumps(r.json())
    return render_template('index.html', username=username, project_id=project_id, items=r.json(),
                           api_url=app.config['API_URL'])
