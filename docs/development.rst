Development
===========

.. highlight:: bash

Getting the source code
-----------------------
The source code is maintained in the Dataflake Git repository.
To check out the trunk::

  $ git clone https://git.dataflake.org/git/Products.LDAPMultiPlugins

You can also browse the code online at 
http://git.dataflake.org/cgit/Products.LDAPMultiPlugins

Bug tracker
-----------
For bug reports, suggestions or questions please use the 
Launchpad bug tracker at 
`https://bugs.launchpad.net/products.ldapmultiplugins 
<https://bugs.launchpad.net/products.ldapmultiplugins>`_.

Setting up a development sandbox and testing
--------------------------------------------
Once you've obtained a source checkout, you can follow these
instructions to perform various development tasks.
All development requires that you run the buildout from the 
package root directory::

  $ python bootstrap.py
  $ bin/buildout

Once you have a buildout, the tests can be run as follows::

  $ bin/test

Building the documentation
--------------------------
The Sphinx documentation is built by doing the following from the
directory containing setup.py::

  $ cd docs
  $ make html

Making a release
----------------
The first thing to do when making a release is to check that the ReST
to be uploaded to PyPI is valid::

  $ bin/docpy setup.py --long-description | bin/rst2 html \
    --link-stylesheet \
    --stylesheet=http://www.python.org/styles/styles.css > build/desc.html

Once you're certain everything is as it should be, the following will
build the distribution, upload it to PyPI, register the metadata with
PyPI and upload the Sphinx documentation to PyPI::

  $ bin/buildout -o
  $ bin/docpy setup.py sdist register upload upload_sphinx --upload-dir=docs/_build/html

The ``bin/buildout`` will make sure the correct package information is
used.

