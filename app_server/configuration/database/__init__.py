# -*- coding: UTF-8 -*-

"""
 Module
     __init__.py
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
     Defined class BaseConfig with attribute(s) and method(s).
     Base initial configuration for database.
"""

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, https://vroncevic.github.io/config_flask"
__credits__ = ["Vladimir Roncevic"]
__license__ = "https://github.com/vroncevic/config_flask/blob/master/LICENSE"
__version__ = "1.2.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class BaseConfig(object):
    """
        Defined class BaseConfig with attribute(s) and method(s).
        Base initial configuration for database.
        It defines:

            :attributes:
                | SQLALCHEMY_TRACK_MODIFICATIONS - Requires extra memory (True)
            :methods:
                | None
    """

    SQLALCHEMY_TRACK_MODIFICATIONS = False
