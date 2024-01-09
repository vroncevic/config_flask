# -*- coding: UTF-8 -*-

'''
Module
    db_conf_dev_mode_test.py
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
    Defines class DBDevTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of database configuration.
Execute
    python3 -m unittest -v db_conf_dev_mode_test
'''

import sys
from typing import List
import unittest

try:
    from app_server.configuration.database.dev_config import DevConfig
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


class DBDevTestCase(unittest.TestCase):
    '''
        Defines class DBDevTestCase with attribute(s) and method(s).
        Creates test cases for checking of database configuration.

        It defines:

            :attributes:
                | track_modifications - Test track modifications check.
                | db_user - Test db user check.
                | db_password - Test db password check.
                | db_host - Test db host check.
                | db_port - Test db port check.
                | db_dialect - Test db dialect check.
                | sqlalchemy_database_uri - Test sqlalchemy database uri check.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_track_modifications - Track modifications check.
                | test_db_user - Test test db user check.
                | test_db_password - Test db password check.
                | test_db_host - Test db host check.
                | test_db_port - Test db port check.
                | test_db_dialect - Test db dialect check.
                | test_database_uri - Test sqlalchemy database uri check.
    '''

    def setUp(self):
        '''Call before test case.'''
        self.track_modifications = DevConfig.SQLALCHEMY_TRACK_MODIFICATIONS
        self.db_user = DevConfig.DB_USER
        self.db_password = DevConfig.DB_PASSWORD
        self.db_host = DevConfig.DB_HOST
        self.db_port = DevConfig.DB_PORT
        self.db_dialect = DevConfig.DB_DIALECT
        self.sqlalchemy_database_uri = DevConfig.SQLALCHEMY_DATABASE_URI

    def tearDown(self):
        '''Call after test case.'''
        self.track_modifications = None
        self.db_user = None
        self.db_password = None
        self.db_host = None
        self.db_port = None
        self.db_dialect = None
        self.sqlalchemy_database_uri = None

    def test_track_modifications(self):
        '''Test sqlalchemy track modifications check.'''
        self.assertEqual(self.track_modifications, False)

    def test_db_user(self):
        '''Test db user check.'''
        self.assertEqual(isinstance(self.db_user, str), True)

    def test_db_password(self):
        '''Test db password check.'''
        self.assertEqual(isinstance(self.db_password, str), True)

    def test_db_host(self):
        '''Test db host check.'''
        self.assertEqual(isinstance(self.db_host, str), True)

    def test_db_port(self):
        '''Test db port check.'''
        self.assertEqual(self.db_port, 3306)

    def test_db_dialect(self):
        '''Test db dialect check.'''
        self.assertEqual(isinstance(self.db_dialect, str), True)

    def test_database_uri(self):
        '''Test sqlalchemy database uri check.'''
        self.assertEqual(isinstance(self.sqlalchemy_database_uri, str), True)


if __name__ == '__main__':
    unittest.main()
