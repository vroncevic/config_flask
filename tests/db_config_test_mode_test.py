# -*- coding: UTF-8 -*-

'''
Module
    db_config_test_mode_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    config_flask is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    config_flask is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class DBTestTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of database configuration.
Execute
    python3 -m unittest -v db_config_test_mode_test
'''

import sys
from typing import List
import unittest

try:
    from app_server.configuration.database.test_config import TestConfig
except ImportError as test_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/config_flask'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.8.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DBTestTestCase(unittest.TestCase):
    '''
        Defines class DBTestTestCase with attribute(s) and method(s).
        Creates test cases for checking of database configuration.

        It defines:

            :attributes:
                | track_modifications - Test track modifications check.
                | sqlalchemy_database_uri - Test sqlalchemy database uri check.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_track_modifications - Test track modifications check.
                | test_database_uri - Test database uri check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.track_modifications = TestConfig.SQLALCHEMY_TRACK_MODIFICATIONS
        self.sqlalchemy_database_uri = TestConfig.SQLALCHEMY_DATABASE_URI

    def tearDown(self):
        '''Call after test case.'''
        self.track_modifications = None
        self.sqlalchemy_database_uri = None

    def test_track_modifications(self):
        '''Test sqlalchemy track modifications check.'''
        self.assertEqual(self.track_modifications, False)

    def test_database_uri(self):
        '''Test sqlalchemy database uri check.'''
        self.assertEqual(isinstance(self.sqlalchemy_database_uri, str), True)


if __name__ == '__main__':
    unittest.main()
