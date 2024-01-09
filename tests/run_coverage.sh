#!/bin/bash
#
# @brief   config_flask
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2017
# @company None, free software to use 2017
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 -m coverage run -m --source=../app_server unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
