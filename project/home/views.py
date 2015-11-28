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
import os,json
from project import app
from base64 import b64encode
from project import ifcopenshell as ifc
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
        user_id = "abcdef"
        username = "lorinma"
        email = "malingreal@gmail.com"
    else:
        username = user.given_name
        email = user.email
        user_id = user.get_id()[-22:]
    description = "test"
    
################
#### test ####
################
    project_id = ""
    r = requests.get(app.config['MONGODB_URL']+"/project?user_id="+user_id)
    project_items=r.json()
    if len(project_items['_items'])==0:
        r = requests.post(app.config['MONGODB_URL']+"/project", data = {"username":username,"email":email,"user_id":user_id,"description":description})
        project_items=r.json()
        project_id=project_items["_id"]
    else:
        project_info = project_items['_items'][0]
        project_id =  project_info['_id']
################
#### test ####
################
    r = requests.get(app.config['MONGODB_URL']+"/file?project_id="+project_id)
    return render_template('index.html', username=username, project_id=project_id, items=r.json(), db_url=app.config['MONGODB_URL'])
    
@home_blueprint.route('/upload')  # pragma: no cover
@login_required  # pragma: no cover
def upload():
    headers = {'Content-Type': 'application/json'}
    project_id="5658757ad737bd5ec6b49832"
        
################
#### test ####
################
    project_id = request.args.get('project_id')
    url = request.args.get('url')
    url = url[:-1]+'1'
    r = requests.get(url)
    filename = request.args.get('filename')
    path = os.path.join(app.config['APP_TEMP_FILE'], b64encode(filename)+".ifc")
    with open(path, 'wb') as f:
        f.write(r.content)
    
#### test ####
    # filename = "test.ifc"
    # path = os.path.join(app.config['APP_TEMP_FILE'], "test.ifc")
#### test ####

################
#### test ####
################
    r = requests.post(app.config['MONGODB_URL']+"/file", data = {"project_id":project_id , "filename":filename})
    response_data=r.json()
    file_id=response_data['_id']
    
#### test ####
    # file_id = "5654bfa9d737bd7e94b37e6c"
#### test ####
    
    file = ifc.open(path)
    # get all the entities line_ids
    num=file.wrapped_data.entity_names()
    data=list()
    
    for i in num:
        entity = file.wrapped_data.by_id(i)
        entity_data = {"line_id":entity.id(),"type": entity.is_a(),"content": entity.__str__(),"file_id":file_id, "project_id":file_id}
        for j in xrange(entity.__len__()):
            try:
                entity_data[entity.get_argument_name(j)]=entity.get_argument(j).id()
            except:
                import types
                if isinstance(entity.get_argument(j), list):
                    entity_data[entity.get_argument_name(j)]=list()
                    for v in entity.get_argument(j):
                        try:
                            entity_data[entity.get_argument_name(j)].append(v.id())
                        except:
                            entity_data[entity.get_argument_name(j)].append(v)
                else:
                    entity_data[entity.get_argument_name(j)]=entity.get_argument(j)
        data.append(entity_data)

    r = requests.post(app.config['MONGODB_URL']+"/entity",headers=headers, data = json.dumps(data))
    
# #### test ####
#     response_data=r.json()
#     return json.dumps(response_data)
# #### test ####

    os.remove(path)
    return jsonify(filename=filename,file_id=file_id)

# if you are going to fetch repeatedly from name, you better construct a dictionary with the names as keys so get operations are O(1)
def build_dict(seq, key):
    return dict((d[key], dict(d, index=i)) for (i, d) in enumerate(seq))