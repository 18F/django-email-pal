Developing django-email-pal
===========================

.. important::

    This section is about developing django-email-pal
    itself, not using it in your Django project. For
    details on the latter, see the :doc:`quickstart`.

.. highlight:: none

First, clone the git repository::

    git clone https://github.com/18F/django-email-pal

Then create a virtualenv for the project and install
development dependencies::

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

Then install django-email-pal in development mode::

    python setup.py develop

Running tests
-------------

You can run all the tests with code coverage::

    pytest

You can also ensure that there aren't any linting errors::

    flake8

To run all tests, linters, and other automated QA against
all supported runtimes and dependencies, run::

    tox

Writing documentation
---------------------

If you want to work on documentation, you can run the development
documentation server with::

    python setup.py devdocs

Template Information
--------------------
:ref:`Base Template Documentation`
