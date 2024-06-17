# Flask Configuration Mechanism

<img align="right" src="https://raw.githubusercontent.com/vroncevic/config_flask/dev/docs/config_flask_logo.png" width="25%">

**config_flask** is toolset for configuration setup of Flask App.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![config_flask_python_checker](https://github.com/vroncevic/config_flask/actions/workflows/config_flask_python_checker.yml/badge.svg)](https://github.com/vroncevic/config_flask/actions/workflows/config_flask_python_checker.yml) [![config_flask_package_checker](https://github.com/vroncevic/config_flask/actions/workflows/config_flask_package_checker.yml/badge.svg)](https://github.com/vroncevic/config_flask/actions/workflows/config_flask_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/config_flask.svg)](https://github.com/vroncevic/config_flask/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/config_flask.svg)](https://github.com/vroncevic/config_flask/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/ats_utilities/dev/docs/debtux.png)

Navigate to **[release page](https://github.com/vroncevic/config_flask/releases)** download and extract release archive.

To install **config_flask** type the following

```bash
tar xvzf config_flask-x.y.z.tar.gz
mv config_flask-x.y.z/app_server/configuration /FlaskApp/app_server/
```

Or You can use docker to create image/container.

### Dependencies

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

### Package structure

Expected configuration structure

```bash
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
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/config-flask/badge/?version=latest)](https://config-flask.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [config_flask.readthedocs.io](https://config-flask.readthedocs.io/)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to config_flask](CONTRIBUTING.md)

### Copyright and Licence

[![license: gpl v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![license apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/config_flask](https://vroncevic.github.io/config_flask/)

**config_flask** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/config_flask/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
