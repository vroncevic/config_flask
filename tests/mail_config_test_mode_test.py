# -*- coding: UTF-8 -*-

'''
Module
    mail_config_test_mode_test.py
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
    Defines class MailTestTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of mail configuration.
Execute
    python3 -m unittest -v mail_config_test_mode_test
'''

import sys
from typing import List
import unittest

try:
    from app_server.configuration.mail.test_config import TestConfig
except ImportError as test_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/config_flask'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.8.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class MailTestTestCase(unittest.TestCase):
    '''
        Defines class MailTestTestCase with attribute(s) and method(s).
        Creates test cases for checking of mail configuration.

        It defines:

            :attributes:
                | mail_server - Test mail server check.
                | mail_port - Test mail port check.
                | mail_use_ssl - Test mail use ssl check.
                | mail_username - Test mail username check.
                | mail_password - Test mail password check.
                | mail_recipient - Test mail recipient check.
            :methods:
                | setUp - Call before test cases.
                | tearDown - Call after test cases.
                | test_mail_server - Test mail server check.
                | test_mail_port - Test mail port check.
                | test_mail_use_ssl - Test mail use ssl check.
                | test_mail_username - Test mail username check.
                | test_mail_password - Test mail password check.
                | test_mail_recipient - Test mail recipient check.
    '''

    def setUp(self) -> None:
        '''Call before test cases.'''
        self.mail_server: str | None = TestConfig.MAIL_SERVER
        self.mail_port: int | None = TestConfig.MAIL_PORT
        self.mail_use_ssl: bool | None = TestConfig.MAIL_USE_SSL
        self.mail_username: str | None = TestConfig.MAIL_USERNAME
        self.mail_password: str | None = TestConfig.MAIL_PASSWORD
        self.mail_recipient: str | None = TestConfig.MAIL_RECIPIENT

    def tearDown(self) -> None:
        '''Call after test cases.'''
        self.mail_server = None
        self.mail_port = None
        self.mail_use_ssl = None
        self.mail_username = None
        self.mail_password = None
        self.mail_recipient = None

    def test_mail_server(self) -> None:
        '''Test mail server check.'''
        self.assertEqual(isinstance(self.mail_server, str), True)

    def test_mail_port(self) -> None:
        '''Test mail port check.'''
        self.assertEqual(self.mail_port, 465)

    def test_mail_use_ssl(self) -> None:
        '''Test mail use ssl check.'''
        self.assertEqual(self.mail_use_ssl, True)

    def test_mail_username(self) -> None:
        '''Test mail username check.'''
        self.assertEqual(isinstance(self.mail_username, str), True)

    def test_mail_password(self) -> None:
        '''Test mail password check.'''
        self.assertEqual(isinstance(self.mail_password, str), True)

    def test_mail_recipient(self) -> None:
        '''Test mail received check.'''
        self.assertEqual(isinstance(self.mail_recipient, str), True)


if __name__ == '__main__':
    unittest.main()
