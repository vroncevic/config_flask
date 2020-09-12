Flask Configuration Mechanism
------------------------------

**config_flask** is toolset for configuration setup of Flask App.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/config_flask/workflows/Python%20package/badge.svg
   :target: https://github.com/vroncevic/config_flask/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/config_flask.svg
   :target: https://github.com/vroncevic/config_flask/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/config_flask.svg
   :target: https://github.com/vroncevic/config_flask/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/config_flask/badge/?version=latest
   :target: https://config_flask.readthedocs.io/projects/config_flask/en/latest/?badge=latest

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   self
   modules

Installation
-------------

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/config_flask/releases

To install modules type the following:

.. code-block:: bash

    tar xvzf config_flask-x.y.z.tar.gz
    mv config_flask-x.y.z/app_server/configuration /FlaskApp/app_server/

Dependencies
-------------

**config_flask** requires other modules and libraries:

    * none

Package structure
------------------

Expected configuration structure:

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

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/config_flask <https://vroncevic.github.io/config_flask>`_

**config_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
