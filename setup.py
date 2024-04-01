# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netlab',
 'netlab.api',
 'netlab.cli',
 'netlab.datatypes',
 'netlab.enums',
 'netlab.errors']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'importlib-metadata>=4.13.0,<5.0.0',
 'packaging>=21.3,<22.0',
 'tabulate>=0.8,<0.9',
 'typing-extensions>=3.10.0,<4.0.0']

entry_points = \
{'console_scripts': ['netlab = netlab.cli:main']}

setup_kwargs = {
    'name': 'netlab',
    'version': '22.4.0',
    'description': 'NETLAB+ VE SDK for Python',
    'long_description': '# OVERVIEW\n\n[![pipeline status](https://gitlab.netdevgroup.com/dev/netlab-ve-api-py/badges/master/pipeline.svg)](https://gitlab.netdevgroup.com/dev/netlab-ve-api-py/-/pipelines?scope=all&ref=master)\n[![coverage report](https://gitlab.netdevgroup.com/dev/netlab-ve-api-py/badges/master/coverage.svg)](https://gitlab.netdevgroup.com/dev/netlab-ve-api-py/-/commits/master)\n[![downloads](https://img.shields.io/endpoint?url=https://ndg.tech/api/badges/netlab-py-latest/)](https://portal.netdevgroup.com/staff/tech/url/netlab-py-latest)\n[![python versions](https://shields.io/badge/python-3.7%20|%203.8%20|%203.9%20|%203.10-brightgreen)](https://gitlab.netdevgroup.com/dev/netlab-ve-api-py/-/blob/master/tox.ini)\n\nThe goal of this project is to provide a mechanism for NETLAB+ administrators to\nprogramatically manage his or her NETLAB+ appliance.\n\nPython is the language of choice for creating API calls directly to NETLAB+.\nWith this package you will be able to manipulate (add/create, update, delete,\nget/list) user\'s, pod\'s, classes, vm\'s, reservations and more.\n\n\n# INSTALL\n\n    pip install https://ndg.tech/netlab-py-latest\n\n\n# LICENSE\n\nMIT License\n\nCopyright (c) 2017 Network Development Group, Inc\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\ndocumentation files (the "Software"), to deal in the Software without restriction, including without limitation\nthe rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and\nto permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of\nthe Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\nWARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS\nOR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR\nOTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n',
    'author': 'Aaron Schif',
    'author_email': 'aschif@netdevgroup.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.netdevgroup.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
