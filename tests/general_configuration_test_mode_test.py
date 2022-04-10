# -*- coding: UTF-8 -*-

'''
 Module
     general_configuration_test_mode_test.py
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
     Defined class GeneralConfigTestTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of general configuration.
 Execute
     python3 -m unittest -v general_configuration_test_mode_test
'''

import sys
import unittest

try:
    from app_server.configuration.test_config import TestConfig
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/config_flask'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.5.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GeneralConfigTestTestCase(unittest.TestCase):
    '''
        Defined class GeneralConfigTestTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of A1z52N62.
        It defines:

            :attributes:
                | debug - debug enabled.
                | wtf_csrf_enabled - CSRF enabled.
                | debug_tb_enabled - Debug TB enabled.
                | debug_tb_intercept_redirects - DEBUG TB INTERCEPT REDIRECTS enabled.
                | bcrypt_log_rounds - BCRYPT LOG ROUNDS setup.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_debug - test debug check.
                | test_wtf_csrf_enabled - test CSRF check.
                | test_debug_tb_enabled - test DEBUG TB check.
                | test_debug_tb_intercept_redirects - test DEBUG TB INTERCEPT REDIRECTS check.
                | test_bcrypt_log_rounds - test BCRYPT LOG ROUNDS check.
    '''

    def setUp(self):
        '''Call before test cases.'''
        self.debug = TestConfig.DEBUG
        self.wtf_csrf_enabled = TestConfig.WTF_CSRF_ENABLED
        self.debug_tb_enabled = TestConfig.DEBUG_TB_ENABLED
        self.debug_tb_intercept_redirects = TestConfig.DEBUG_TB_INTERCEPT_REDIRECTS
        self.bcrypt_log_rounds = TestConfig.BCRYPT_LOG_ROUNDS

    def tearDown(self):
        '''Call after test cases.'''
        self.debug = None
        self.wtf_csrf_enabled = None
        self.debug_tb_enabled = None
        self.debug_tb_intercept_redirects = None
        self.bcrypt_log_rounds = None

    def test_debug(self):
        '''Test debug check.'''
        self.assertEqual(self.debug, True)

    def test_wtf_csrf_enabled(self):
        '''Test CSRF check.'''
        self.assertEqual(self.wtf_csrf_enabled, False)

    def test_debug_tb_enabled(self):
        '''Test DEBUG TB check.'''
        self.assertEqual(self.debug_tb_enabled, True)

    def test_debug_tb_intercept_redirects(self):
        '''Test DEBUG TB INTERCEPT REDIRECTS check.'''
        self.assertEqual(self.debug_tb_intercept_redirects, True)

    def test_bcrypt_log_rounds(self):
        '''Test BCRYPT LOG ROUNDS check.'''
        self.assertEqual(self.bcrypt_log_rounds, 4)

if __name__ == '__main__':
    unittest.main()
