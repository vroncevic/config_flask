# -*- coding: UTF-8 -*-

"""
 Module
     development_config.py
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
     Defined class DevelopmentConfig with attribute(s) and method(s).
     Development configuration.
"""

import sys

try:
    from app_server.configuration.database import BaseConfig
except ImportError as ats_error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, https://vroncevic.github.io/config_flask"
__credits__ = ["Vladimir Roncevic"]
__license__ = "https://github.com/vroncevic/config_flask/blob/dev/LICENSE"
__version__ = "1.3.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class DevelopmentConfig(BaseConfig):
    """
        Defined class DevelopmentConfig with attribute(s) and method(s).
        Development database configuration.
        It defines:

            :attributes:
                | DB_USER - database connection username.
                | DB_PASSWORD - database connection user password.
                | DB_HOST - database server address.
                | DB_PORT - database server port.
                | DB_DIALECT - database dialect prefix.
                | SQLALCHEMY_DATABASE_URI - set DB URI.
            :methods:
                | None
    """

    DB_USER = "mydbuser"
    DB_PASSWORD = "mydbpassword"
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_NAME = "manage_users"
    DB_DIALECT = "mysql+mysqlconnector"
    SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(
        DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )
