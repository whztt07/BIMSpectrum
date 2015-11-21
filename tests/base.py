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

import os
from flask.ext.testing import TestCase

from project import app
# from project.models import User, BlogPost


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object(os.environ['APP_SETTINGS'])
        return app

    def setUp(self):
    # db.create_all()
    # db.session.add(User("admin", "ad@min.com", "admin"))
    # db.session.add(
    #     BlogPost("Test post", "This is a test. Only a test.", "admin"))
    # db.session.commit()
        pass

    def tearDown(self):
    # db.session.remove()
    # db.drop_all()
        pass


    # She needs to login at the homepage through stormpath.com

    # After authentication, she can then login his dropbox and choose a file from her dropbox folder

    # The file should be an IFC file

    # The file will be uploaded to a DB hosted on mongoLab

    # The file will be downloaded to the web service with a Base64 encoded filename

    # The downloaded file then be parsed by ifcopenshell and be decomposed into entities and be sent to mongoDB

    # The web service can delete the file if storage not permitted