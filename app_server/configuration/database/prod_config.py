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
    Production database configuration.
'''

import sys
from typing import List

try:
    from app_server.configuration.database import BaseConfig
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__copyright__ = '(C) 2024, https://vroncevic.github.io/config_flask'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/config_flask/blob/dev/LICENSE'
__version__ = '1.7.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProdConfig(BaseConfig):
    '''
        Defines class ProdConfig with attribute(s) and method(s).
        Production database configuration.

        It defines:

            :attributes:
                | DB_USER - Database connection username.
                | DB_PASSWORD - Database connection user password.
                | DB_HOST - Database server address.
                | DB_PORT - Database server port.
                | DB_DIALECT - Database dialect prefix.
                | SQLALCHEMY_DATABASE_URI - Set DB URI.
            :methods:
                | None
    '''

    DB_USER: str = 'mydbuser'
    DB_PASSWORD: str = 'mydbpassword'
    DB_HOST: str = '127.0.0.1'
    DB_PORT: str = 5432
    DB_NAME: str = 'manage_users'
    DB_DIALECT: str = 'postgresql'
    DB_LOGIN: str = f'{DB_USER}:{DB_PASSWORD}'
    DB_SERVER: str = f'{DB_HOST}:{DB_PORT}'
    SQLALCHEMY_DATABASE_URI: str = f'{DB_DIALECT}://{DB_SERVER}/{DB_NAME}'
