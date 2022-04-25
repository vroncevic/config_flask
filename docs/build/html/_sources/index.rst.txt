Flask Configuration Mechanism
------------------------------

**config_flask** is toolset for configuration setup of Flask App.

Developed in `python <https://www.python.org/>`_ code.

|codecov| |circleci|

.. |codecov| image:: https://codecov.io/gh/vroncevic/config_flask/branch/dev/graph/badge.svg
   :target: https://codecov.io/gh/vroncevic/config_flask

.. |circleci| image:: https://circleci.com/gh/vroncevic/config_flask/tree/master.svg
   :target: https://circleci.com/gh/vroncevic/config_flask/tree/master

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|python checker| |python package| |github issues| |documentation status| |github contributors|

.. |python checker| image:: https://img.shields.io/github/workflow/status/vroncevic/config_flask/config_flask_python_checker?style=flat&label=config_flask%20python%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/config_flask/config_flask_python_checker

.. |python package| image:: https://img.shields.io/github/workflow/status/vroncevic/config_flask/config_flask_package_checker?style=flat&label=config_flask%20package%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/config_flask/config_flask_package_checker

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/config_flask.svg
   :target: https://github.com/vroncevic/config_flask/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/config_flask.svg
   :target: https://github.com/vroncevic/config_flask/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/config_flask/badge/?version=master
   :target: https://config_flask.readthedocs.io/projects/config_flask/en/master/?badge=master

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|ubuntu linux os|

.. |ubuntu linux os| image:: https://raw.githubusercontent.com/vroncevic/config_flask/dev/docs/ubuntuxis.png

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/config_flask/releases

To install modules type the following

.. code-block:: bash

    tar xvzf config_flask-x.y.z.tar.gz
    mv config_flask-x.y.z/app_server/configuration /FlaskApp/app_server/

You can use Docker to create image/container.

|github docker checker|

.. |github docker checker| image:: https://img.shields.io/github/workflow/status/vroncevic/config_flask/config_flask_docker_checker?style=flat&label=config_flask%20docker%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/config_flask/config_flask_docker_checker

Dependencies
-------------

**config_flask** requires other modules and libraries

    * none

Package structure
------------------

Expected configuration structure

.. code-block:: bash

    app_server/
    ├── configuration/
    │   ├── database/
    │   │   ├── development_config.py
    │   │   ├── __init__.py
    │   │   ├── production_config.py
    │   │   └── test_config.py
    │   ├── development_config.py
    │   ├── __init__.py
    │   ├── mail/
    │   │   ├── development_config.py
    │   │   ├── __init__.py
    │   │   ├── production_config.py
    │   │   └── test_config.py
    │   ├── production_config.py
    │   └── test_config.py
    └── __init__.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/config_flask <https://vroncevic.github.io/config_flask>`_

**config_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/config_flask/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
