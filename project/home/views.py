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


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, jsonify, url_for
from flask.ext.stormpath import login_required,user
import requests
import os
from project import app
from base64 import b64encode
################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)   # pragma: no cover


################
#### routes ####
################

# use decorators to link the function to a url
@home_blueprint.route('/')   # pragma: no cover
@login_required # pragma: no cover 
def home():
    if app.config['TESTING'] == True:
        email = "malingreal@gmail.com"
        username = "Ling"
    else:
        email = user.email
        username = user.given_name
    r = requests.get(app.config['MONGODB_URL']+"/file?where=email=='"+email+"'")
    return render_template('index.html', username=username, items=r.json(), db_url=app.config['MONGODB_URL'])
    
@home_blueprint.route('/upload')  # pragma: no cover
@login_required  # pragma: no cover
def upload():
    if app.config['TESTING'] == True:
        email = "malingreal@gmail.com"
        username = "Ling"
    else:
        email = user.email
        username = user.given_name
    url = request.args.get('url')
    url = url[:-1]+'1'
    r = requests.get(url)
    filename = request.args.get('filename')
    path = os.path.join(app.config['APP_TEMP_FILE'], b64encode(filename)+".ifc")
    with open(path, 'wb') as f:
        f.write(r.content)
    r = requests.post(app.config['MONGODB_URL']+"/file", data = {"username":username , "filename":filename, "email":email})
    response_data=r.json()
    os.remove(path)
    return jsonify(filename=filename,fileid=response_data['_id'])
    
