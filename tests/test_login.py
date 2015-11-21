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


class UserTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    #
    # # Ensure that main page requires user login
    # def test_main_route_requires_login(self):
    #     response = self.client.get('/', follow_redirects=True)
    #     self.assertIn(b'Please log in to access this page', response.data)
    #
    # # Ensure that welcome page loads
    # def test_welcome_route_works_as_expected(self):
    #     response = self.client.get('/welcome', follow_redirects=True)
    #     self.assertIn(b'Welcome to Flask!', response.data)
    #
    # # Ensure that posts show up on the main page
    # def test_posts_show_up_on_main_page(self):
    #     response = self.client.post(
    #         '/login',
    #         data=dict(username="admin", password="admin"),
    #         follow_redirects=True
    #     )
    #     self.assertIn(b'This is a test. Only a test.', response.data)

if __name__ == '__main__':
    unittest.main()