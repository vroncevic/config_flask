# -*- coding: UTF-8 -*-

'''
Module
    prod_config.py
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
    Defines class ProdConfig with attribute(s) and method(s).
    Production configuration.
'''

import sys
from typing import List

try:
    from app_server.configuration import BaseConfig
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/config_flask'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.8.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProdConfig(BaseConfig):
    '''
        Defines class ProdConfig with attribute(s) and method(s).
        Production configuration.

        It defines:

            :attributes:
                | DEBUG - Enable/Disable debug option.
                | WTF_CSRF_ENABLED - Secure forms.
                | DEBUG_TB_ENABLED - Flask debug toolbar's.
                | DEBUG_TB_INTERCEPT_REDIRECTS - Should intercept redirects.
                | BCRYPT_LOG_ROUNDS - For bcrypt hashing utilities.
            :methods:
                | None
    '''

    DEBUG: bool = False
    WTF_CSRF_ENABLED: bool = True
    DEBUG_TB_ENABLED: bool = False
    DEBUG_TB_INTERCEPT_REDIRECTS: bool = False
    BCRYPT_LOG_ROUNDS: int = 4
