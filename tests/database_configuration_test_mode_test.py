# -*- coding: UTF-8 -*-

'''
 Module
     database_configuration_test_mode_test.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class DatabaseTestTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of database configuration.
 Execute
     python3 -m unittest -v database_configuration_test_mode_test
'''

import sys
import unittest

try:
    from app_server.configuration.database.test_config import TestConfig
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/config_flask'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DatabaseTestTestCase(unittest.TestCase):
    '''
        Defined class DatabaseTestTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of database configuration.
        It defines:

            :attributes:
                | sqlalchemy_track_modifications - test sqlalchemy track modifications check.
                | sqlalchemy_database_uri - test sqlalchemy database uri check.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_sqlalchemy_track_modifications - test sqlalchemy track modifications check.
                | test_sqlalchemy_database_uri - test sqlalchemy database uri check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.sqlalchemy_track_modifications = TestConfig.SQLALCHEMY_TRACK_MODIFICATIONS
        self.sqlalchemy_database_uri = TestConfig.SQLALCHEMY_DATABASE_URI

    def tearDown(self):
        '''Call after test case.'''
        self.sqlalchemy_track_modifications = None
        self.sqlalchemy_database_uri = None

    def test_sqlalchemy_track_modifications(self):
        '''Test sqlalchemy track modifications check.'''
        self.assertEqual(self.sqlalchemy_track_modifications, False)

    def test_sqlalchemy_database_uri(self):
        '''Test sqlalchemy database uri check.'''
        self.assertEqual(isinstance(self.sqlalchemy_database_uri, str), True)


if __name__ == '__main__':
    unittest.main()
