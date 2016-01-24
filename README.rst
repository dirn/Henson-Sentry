=============
Henson-Sentry
=============

A library for integrating Sentry into a Henson application.

Installation
============

.. code::

    $ python -m pip install Henson-Sentry

Quickstart
==========

.. code::

    from henson import Application
    from henson_sentry import Sentry

    app = Application('application-with-sentry')
    Sentry(app)
