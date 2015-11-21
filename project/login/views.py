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

from flask.ext.stormpath import StormpathManager
from flask import Blueprint,render_template
from project import app
################
#### config ####
################

login_blueprint = Blueprint(
    'login', __name__,
    template_folder='templates'
)   # pragma: no cover

stormpath_manager = StormpathManager()

# some code which creates your app
stormpath_manager.init_app(app)


# use decorators to link the function to a url
@login_blueprint.route('/welcome')   # pragma: no cover
# @login_required
def home():
    return render_template('welcome.html')