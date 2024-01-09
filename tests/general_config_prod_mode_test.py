# -*- coding: UTF-8 -*-

'''
Module
    general_config_prod_mode_test.py
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
    Defines class GenConfigProdTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of general configuration.
Execute
    python3 -m unittest -v general_config_prod_mode_test
'''

import sys
from typing import List
import unittest

try:
    from app_server.configuration.prod_config import ProdConfig
except ImportError as test_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/config_flask'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.7.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenConfigProdTestCase(unittest.TestCase):
    '''
        Defines class GenConfigProdTestCase with attribute(s) and method(s).
        Creates test cases for checking of general configuration.

        It defines:

            :attributes:
                | debug - Debug enabled.
                | wtf_csrf_enabled - CSRF enabled.
                | debug_tb_enabled - Debug TB enabled.
                | debug_tbir - DEBUG TB INTERCEPT REDIRECTS enabled.
                | bcrypt_log_rounds - BCRYPT LOG ROUNDS setup.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_debug - Test debug check.
                | test_wtf_csrf_enabled - Test CSRF check.
                | test_debug_tb_enabled - Test DEBUG TB check.
                | test_debug_tbir - Test DEBUG TB INTERCEPT REDIRECTS check.
                | test_bcrypt_log_rounds - Test BCRYPT LOG ROUNDS check.
    '''

    def setUp(self):
        '''Call before test cases.'''
        self.debug = ProdConfig.DEBUG
        self.wtf_csrf_enabled = ProdConfig.WTF_CSRF_ENABLED
        self.debug_tb_enabled = ProdConfig.DEBUG_TB_ENABLED
        self.debug_tbir = ProdConfig.DEBUG_TB_INTERCEPT_REDIRECTS
        self.bcrypt_log_rounds = ProdConfig.BCRYPT_LOG_ROUNDS

    def tearDown(self):
        '''Call after test cases.'''
        self.debug = None
        self.wtf_csrf_enabled = None
        self.debug_tb_enabled = None
        self.debug_tbir = None
        self.bcrypt_log_rounds = None

    def test_debug(self):
        '''Test debug check.'''
        self.assertEqual(self.debug, False)

    def test_wtf_csrf_enabled(self):
        '''Test CSRF check.'''
        self.assertEqual(self.wtf_csrf_enabled, True)

    def test_debug_tb_enabled(self):
        '''Test DEBUG TB check.'''
        self.assertEqual(self.debug_tb_enabled, False)

    def test_debug_tbir(self):
        '''Test DEBUG TB INTERCEPT REDIRECTS check.'''
        self.assertEqual(self.debug_tbir, False)

    def test_bcrypt_log_rounds(self):
        '''Test BCRYPT LOG ROUNDS check.'''
        self.assertEqual(self.bcrypt_log_rounds, 4)


if __name__ == '__main__':
    unittest.main()
