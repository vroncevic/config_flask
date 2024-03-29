# -*- coding: UTF-8 -*-

'''
Module
    production_config.py
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
    Defines mail production configuration.
'''

import sys
from typing import List

try:
    from app_server.configuration.mail import BaseConfig
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/config_flask'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.8.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProdConfig(BaseConfig):
    '''
        Defines class ProdConfig with attribute(s) and method(s).
        Defines mail production configuration.

        It defines:

            :attributes:
                | MAIL_USERNAME - Mail username.
                | MAIL_PASSWORD - Mail password.
                | MAIL_RECIPIENT - Mail username.
            :methods:
                | None
    '''

    MAIL_USERNAME: str = ''
    MAIL_PASSWORD: str = ''
    MAIL_RECIPIENT: str = ''
