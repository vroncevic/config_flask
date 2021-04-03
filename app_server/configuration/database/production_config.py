# -*- coding: UTF-8 -*-

"""
 Module
     production_config.py
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
     Defined class ProductionConfig with attribute(s) and method(s).
     Production database configuration.
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
__license__ = "https://github.com/vroncevic/config_flask/blob/master/LICENSE"
__version__ = "1.2.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class ProductionConfig(BaseConfig):
    """
        Defined class ProductionConfig with attribute(s) and method(s).
        Production database configuration.
        It defines:

            :attributes:
                | DB_USER - Database connection username
                | DB_PASSWORD - Database connection user password
                | DB_HOST - Database server address
                | DB_PORT - Database server port
                | DB_DIALECT - Database dialect prefix
                | SQLALCHEMY_DATABASE_URI - Set DB URI
            :methods:
                | None
    """

    DB_USER = "mydbuser"
    DB_PASSWORD = "mydbpassword"
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432
    DB_NAME = "manage_users"
    DB_DIALECT = "postgresql"
    SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}:{4}/{5}".format(
        DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    )
