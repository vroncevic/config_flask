# -*- coding: UTF-8 -*-

'''
 Module
     test_config.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class TestConfig with attribute(s) and method(s).
     Test configuration.
'''

import sys

try:
    from app_server.configuration import BaseConfig
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/config_flask'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.5.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestConfig(BaseConfig):
    '''
        Defined class TestConfig with attribute(s) and method(s).
        Test configuration.
        It defines:

            :attributes:
                | DEBUG - enable/Disable debug option.
                | WTF_CSRF_ENABLED - secure forms.
                | DEBUG_TB_ENABLED - flask debug toolbar's.
                | DEBUG_TB_INTERCEPT_REDIRECTS - should intercept redirects.
                | BCRYPT_LOG_ROUNDS - for bcrypt hashing utilities.
            :methods:
                | None
    '''

    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = True
    BCRYPT_LOG_ROUNDS = 4
