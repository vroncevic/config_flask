# Flask Configuration Mechanism.

config_flask is toolset for configuration setup of Flask App.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

Part of Flask Web Project.

![Python package](https://github.com/vroncevic/config_flask/workflows/Python%20package/badge.svg?branch=master)

### INSTALLATION
Navigate to release [page](https://github.com/vroncevic/config_flask/releases/tag/v1.0) download and extract release archive.

To install this set of modules type the following:

```
tar xvzf config_flask-1.0.tar.gz
mv config_flask-1.0/configuration /FlaskApp/
```

### DEPENDENCIES

These modules requires other modules and libraries:

    * none

### PACKAGE STRUCTURE

Expected configuration structure:

```
configuration/
├── database
│   ├── development_config.py
│   ├── __init__.py
│   ├── production_config.py
│   └── test_config.py
├── development_config.py
├── __init__.py
├── mail
│   ├── development_config.py
│   ├── __init__.py
│   ├── production_config.py
│   └── test_config.py
├── production_config.py
└── test_config.py
```

### COPYRIGHT AND LICENCE

Copyright (C) 2018 by https://vroncevic.github.io/config_flask/

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.7.9/3.4.2 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

