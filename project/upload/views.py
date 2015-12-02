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

from flask import Blueprint, request, redirect, jsonify, url_for
from flask.ext.stormpath import login_required,user
import requests
import os,json
from project import app
from base64 import b64encode
from project import ifcopenshell as ifc

import pymongo
from pymongo import MongoClient
client = MongoClient(host='ds055872.mongolab.com', port=55872)
db = client.ifc
db.authenticate("lorinma", "4GqUynt2")

home_blueprint = Blueprint(
    'upload', __name__,
    template_folder='templates'
)   # pragma: no cover

#TODO Heroku doesn't allow store file on server?
def save_file(url,path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)

# parse ifc file get all the data
def parse_ifc(path,additional_data):
    import ifcopenshell as ifc
    file = ifc.open(path)
    num=file.wrapped_data.entity_names()
    data=list()
    for i in num:
        from bson.objectid import ObjectId
        entity = file.wrapped_data.by_id(i)
        entity_data = {"line_id":entity.id(),"_id":ObjectId(),"type": entity.is_a(),"content": entity.__str__()}
        entity_data = {**entity_data,**additional_data}
        data.append(entity_data)
    data_indexed=build_dict(data,key="line_id")
    inx=0
    for i in num:
        entity = file.wrapped_data.by_id(i)
        for j in range(entity.__len__()):
            attribute_name=entity.get_argument_name(j)
            attribute_value=entity.get_argument(j)
            try:
                line_id=attribute_value.id()
                if line_id==0:
                    # some value like IfcMassMeasure(0.), will give id=0, and need to extract the real value
                    data[inx][attribute_name]=attribute_value.get_argument(0)
                else:
                    data[inx][attribute_name]=data_indexed[line_id]["_id"]
            except:
                import types
                if isinstance(attribute_value, list):
                    data[inx][attribute_name]=list()
                    for v in attribute_value:
                        try:
                            line_id=v.id()
                            data[inx][attribute_name].append(data_indexed[line_id]["_id"])
                        except:
                            data[inx][attribute_name].append(v)
                else:
                    data[inx][attribute_name]=attribute_value
        include_list=file.wrapped_data.traverse(entity)
        data[inx]["include"]=list()
        # this will include all the entities that direct/indirect used for it
        for include in include_list:
    # some traverse result may include some value like IfcMassMeasure(0.) which is just a subclass of real and has no line_id
            try:
                line_id=include.id()
                if line_id!=i:
                    data[inx]["include"].append(data_indexed[line_id]["_id"])
            except:
                pass
        inx+=1
    return data
    
# use decorators to link the function to a url
@home_blueprint.route('/upload')  # pragma: no cover
@login_required  # pragma: no cover
def upload():
    headers = {'Content-Type': 'application/json'}
    
    # save file to web server
    url = request.args.get('url')
    url = url[:-1]+'1'
    filename = request.args.get('filename')
    path = os.path.join(app.config['APP_TEMP_FILE'], b64encode(filename)+".ifc")
    save_file(url,filename)
    
    from bson.objectid import ObjectId
    project_id=ObjectId(request.args.get('project_id'))
    file_id=db.entity.insert_one({"project_id":project_id,"filename":filename}).inserted_id
    
    # post entities to mongodb
    data=parse_ifc(path,{'project_id':project_id,'file_id':file_id})
    db.entity.insert_many(data)
    
# #### test ####
#     response_data=r.json()
#     return json.dumps(response_data)
# #### test ####

    os.remove(path)
    return jsonify(filename=filename,file_id=str(file_id))

# if you are going to fetch repeatedly from name, you better construct a dictionary with the names as keys so get operations are O(1)
def build_dict(seq, key):
    return dict((d[key], dict(d, index=i)) for (i, d) in enumerate(seq))