=============
Henson-Sentry
=============

Henson-Sentry is a library that helps to easily incorporate logging to
`Sentry <https://sentry.readthedocs.org>`_ into a
`Henson <https://henson.readthedocs.org>`_ application.

Installation
============

Henson-Sentry can be installed with::

    $ python -m pip install Henson-Sentry

Configuration
=============

The following configuration settings can be added to the application.

+------------------------------+----------------------------------------------+
| ``SENTRY_DSN``               | The data source name used to identify that   |
|                              | Sentry instance to which to send the logs.   |
+------------------------------+----------------------------------------------+
| ``RAVEN_IGNORE_EXCEPTIONS``  | Exception types that will be ignored when    |
|                              | sending exceptions to Sentry.                |
+------------------------------+----------------------------------------------+
| ``SENTRY_AUTO_LOG_STACKS``   | Whether or not to automatically log full     |
|                              | stack traces. Default: ``False``             |
+------------------------------+----------------------------------------------+
| ``SENTRY_EXCLUDE_PATHS``     | Module prefixes that will be ignored when    |
|                              | attempting to discover from which function   |
|                              | the exception originated. Default: ``()``    |
+------------------------------+----------------------------------------------+
| ``SENTRY_INCLUDE_PATHS``     | Module prefixes that will be included when   |
|                              | attempting to discover from which function   |
|                              | the exception originated. Default ``()``     |
+------------------------------+----------------------------------------------+
| ``SENTRY_MAX_LENGTH_LIST``   | The maximum number of items a list-like      |
|                              | container will store. Default ``50``         |
+------------------------------+----------------------------------------------+
| ``SENTRY_MAX_LENGTH_STRING`` | The maximum number of characters of a string |
|                              | that will be stored. Default ``400``         |
+------------------------------+----------------------------------------------+
| ``SENTRY_NAME``              | The name to use to identify the application. |
|                              | If no value is provided, the application's   |
|                              | name will be used.                           |
+------------------------------+----------------------------------------------+
| ``SENTRY_PROCESSORS``        | A list of processors to apply to events      |
|                              | before sending them to Sentry.               |
+------------------------------+----------------------------------------------+
| ``SENTRY_RELEASE``           | The version of the application. Default      |
|                              | ``None``                                     |
+------------------------------+----------------------------------------------+
| ``SENTRY_SITE_NAME``         | The name used to identify the client.        |
|                              | Default ``None``                             |
+------------------------------+----------------------------------------------+
| ``SENTRY_TAGS``              | A mapping of key-value pairs that will be    |
|                              | associated with all events. Default ``None`` |
+------------------------------+----------------------------------------------+
| ``SENTRY_TRANSPORT``         | The HTTP transport class that will be used   |
|                              | to transmit events. Default ``None``         |
+------------------------------+----------------------------------------------+

Usage
=====

.. code::

    from henson import Application
    from henson_sentry import Sentry

    app = Application('application-with-sentry')
    app.settings['SENTRY_DSN'] = 'https://******@app.getsentry.com/1234'

    Sentry(app)

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
