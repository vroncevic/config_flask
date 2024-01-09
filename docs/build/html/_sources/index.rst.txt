Flask Configuration Mechanism
------------------------------

**config_flask** is toolset for configuration setup of Flask App.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|config_flask python checker| |config_flask package checker|

|config_flask github issues| |config_flask github contributors|

|config_flask documentation status|

.. |config_flask python checker| image:: https://github.com/vroncevic/config_flask/actions/workflows/config_flask_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/config_flask/actions/workflows/config_flask_python_checker.yml

.. |config_flask package checker| image:: https://github.com/vroncevic/config_flask/actions/workflows/config_flask_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/config_flask/actions/workflows/config_flask_package.yml

.. |config_flask github issues| image:: https://img.shields.io/github/issues/vroncevic/config_flask.svg
   :target: https://github.com/vroncevic/config_flask/issues

.. |config_flask github contributors| image:: https://img.shields.io/github/contributors/vroncevic/config_flask.svg
   :target: https://github.com/vroncevic/config_flask/graphs/contributors

.. |config_flask documentation Status| image:: https://readthedocs.org/projects/config-flask/badge/?version=latest
   :target: https://config-flask.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/config_flask/releases

To install **config_flask** type the following

.. code-block:: bash

    tar xvzf config_flask-x.y.z.tar.gz
    mv config_flask-x.y.z/app_server/configuration /FlaskApp/app_server/

You can use Docker to create image/container.

Dependencies
-------------

**config_flask** requires other modules and libraries
 * coverage
 * Flask
 * Flask-Migrate
 * Flask-Script
 * Flask-Login
 * Flask-BCrypt
 * Flask-Bootstrap
 * Flask-DebugToolbar
 * Flask-SQLAlchemy
 * Flask-Testing
 * Flask-WTF
 * WTForms

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

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 - 2024 by `vroncevic.github.io/config_flask <https://vroncevic.github.io/config_flask>`_

**config_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/config_flask/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
