# -*- coding: UTF-8 -*-

'''
 Module
     database_configuration_development_mode_test.py
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
     Defined class DatabaseDevelopmentTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of database configuration.
 Execute
     python3 -m unittest -v database_configuration_development_mode_test
'''

import sys
import unittest

try:
    from app_server.configuration.database.development_config import DevelopmentConfig
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/config_flask'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.3.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DatabaseDevelopmentTestCase(unittest.TestCase):
    '''
        Defined class DatabaseDevelopmentTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of database configuration.
        It defines:

            :attributes:
                | sqlalchemy_track_modifications - test sqlalchemy track modifications check.
                | db_user - test db user check. 
                | db_password - test db password check.
                | db_host - test db host check.
                | db_port - test db port check.
                | db_dialect - test db dialect check.
                | sqlalchemy_database_uri - test sqlalchemy database uri check.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_sqlalchemy_track_modifications - test sqlalchemy track modifications check.
                | test_db_user - test test db user check.
                | test_db_password - test db password check.
                | test_db_host - test db host check.
                | test_db_port - test db port check.
                | test_db_dialect - test db dialect check.
                | test_sqlalchemy_database_uri - test sqlalchemy database uri check.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''
        self.sqlalchemy_track_modifications = DevelopmentConfig.SQLALCHEMY_TRACK_MODIFICATIONS
        self.db_user = DevelopmentConfig.DB_USER
        self.db_password = DevelopmentConfig.DB_PASSWORD
        self.db_host = DevelopmentConfig.DB_HOST
        self.db_port = DevelopmentConfig.DB_PORT
        self.db_dialect = DevelopmentConfig.DB_DIALECT
        self.sqlalchemy_database_uri = DevelopmentConfig.SQLALCHEMY_DATABASE_URI

    def tearDown(self) -> None:
        '''Call after test case.'''
        self.sqlalchemy_track_modifications = None
        self.db_user = None
        self.db_password = None
        self.db_host = None
        self.db_port = None
        self.db_dialect = None
        self.sqlalchemy_database_uri = None

    def test_sqlalchemy_track_modifications(self) -> None:
        '''Test sqlalchemy track modifications check.'''
        self.assertEqual(self.sqlalchemy_track_modifications, False)

    def test_db_user(self) -> None:
        '''Test db user check.'''
        self.assertEqual(isinstance(self.db_user, str), True)

    def test_db_password(self) -> None:
        '''Test db password check.'''
        self.assertEqual(isinstance(self.db_password, str), True)

    def test_db_host(self) -> None:
        '''Test db host check.'''
        self.assertEqual(isinstance(self.db_host, str), True)

    def test_db_port(self) -> None:
        '''Test db port check.'''
        self.assertEqual(self.db_port, 3306)

    def test_db_dialect(self) -> None:
        '''Test db dialect check.'''
        self.assertEqual(isinstance(self.db_dialect, str), True)

    def test_sqlalchemy_database_uri(self) -> None:
        '''Test sqlalchemy database uri check.'''
        self.assertEqual(isinstance(self.sqlalchemy_database_uri, str), True)


if __name__ == '__main__':
    unittest.main()
