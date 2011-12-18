##############################################################################
#
# Copyright (c) 2010 Jens Vagelpohl and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

__version__ = '2.0dev'

import os
from setuptools import setup
from setuptools import find_packages

NAME = 'LDAPMultiPlugins'
here = os.path.abspath(os.path.dirname(__file__))

def _read(name):
    f = open(os.path.join(here, name))
    return f.read()

_boundary = '\n' + ('-' * 60) + '\n\n'

setup(name='Products.%s' % NAME,
      version=__version__,
      description='LDAP-backed plugins for the Zope2 PluggableAuthService',
      long_description=( _read('README.txt') 
                       + _boundary
                       + _read('CHANGES.txt')
                       + _boundary
                       + "Download\n========"
                       ),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python :: 2",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
        ],
      keywords='web application server zope zope2 ldap',
      author="Jens Vagelpohl and contributors",
      author_email="jens@dataflake.org",
      url="http://pypi.python.org/pypi/Products.%s" % NAME,
      license="ZPL 2.1 (http://www.zope.org/Resources/License/ZPL-2.1)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      setup_requires=['setuptools-git'],
      install_requires=[
        'setuptools',
        'Zope2',
        'python-ldap >= 2.0.6',
        'Products.LDAPUserFolder >= 2.9',
        'Products.PluggableAuthService >= 1.4.0',
        ],
      extras_require={
          'exportimport': [
                'Products.GenericSetup >= 1.4.0'
                ]
      },
      entry_points="""
      [zope2.initialize]
      Products.%s = Products.%s:initialize
      """ % (NAME, NAME),
      )

