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

import unittest

from base import BaseTestCase


class HomeTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn('welcome', response.data)
    
    # don't know how to test this process
    # # Ensure that one can download a file from given url and remove it
    # # def test_upload(self):
    # #     response = self.client.get('/upload', data=dict(url="http://www.buildingsmart-tech.org/ifc/IFC4/final/html/annex/annex-e/ifc/basic_shape_CSG.ifc",filename="Facade.ifc"), content_type='html/text')
    # #     # self.assertIn(b'Facade.ifc',response.data)
    # #     self.assertIn(b'ISO-10303-21',response.data)

if __name__ == '__main__':
    unittest.main()