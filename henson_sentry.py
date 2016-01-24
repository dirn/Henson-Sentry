"""A Henson plugin to integrate Sentry."""

import asyncio

from henson import Extension
from raven.base import Client
from raven.utils.imports import import_string

__all__ = ('Sentry',)

__version__ = '0.0.1'


class Sentry(Extension):
    """A class to integrate Sentry."""

    DEFAULT_SETTINGS = {
        'RAVEN_IGNORE_EXCEPTIONS': (),
        'SENTRY_AUTO_LOG_STACKS': None,
        'SENTRY_EXCLUDE_PATHS': None,
        'SENTRY_INCLUDE_PATHS': (),
        'SENTRY_MAX_LENGTH_LIST': None,
        'SENTRY_MAX_LENGTH_STRING': None,
        'SENTRY_NAME': None,
        'SENTRY_PROCESSORS': None,
        'SENTRY_RELEASE': None,
        'SENTRY_SITE_NAME': None,
        'SENTRY_TAGS': None,
        'SENTRY_TRANSPORT': None,
    }

    REQUIRED_SETTINGS = (
        'SENTRY_DSN',
    )

    _client = None

    def init_app(self, app):
        """Initialize an ``Application`` instance.

        Args:
            app (henson.base.Application): The application instance to
                be initialized.
        """
        super().init_app(app)

        if not self._client:
            self._client = _make_client(app)

        app.error(self._handle_exception)
        app.message_acknowledgement(self._after_message)

    @asyncio.coroutine
    def capture_exception(self, exc_info=None, **kwargs):
        """Create an event from an exception."""
        self._client.captureException(exc_info, **kwargs)

    @asyncio.coroutine
    def capture_message(self, message, **kwargs):
        """Create an event from ``message``."""
        self._client.captureMessage(message, **kwargs)

    @asyncio.coroutine
    def _after_message(self, app, message):
        print('hi')
        self._client.context.clear()

    @asyncio.coroutine
    def _handle_exception(self, app, message, exc):
        if isinstance(exc, self.app.settings['RAVEN_IGNORE_EXCEPTIONS']):
            return

        yield from self.capture_exception(message=message)


def _make_client(app):
    transport = app.settings['SENTRY_TRANSPORT']
    if isinstance(transport, str):
        transport = import_string(transport)

    return Client(
        dsn=app.settings['SENTRY_DSN'],
        transport=transport,
        include_paths=app.settings['SENTRY_INCLUDE_PATHS'],
        exclude_paths=app.settings['SENTRY_EXCLUDE_PATHS'],
        name=app.settings['SENTRY_NAME'],
        site_name=app.settings['SENTRY_SITE_NAME'],
        processors=app.settings['SENTRY_PROCESSORS'],
        string_max_length=app.settings['SENTRY_MAX_LENGTH_STRING'],
        list_max_length=app.settings['SENTRY_MAX_LENGTH_LIST'],
        auto_log_stacks=app.settings['SENTRY_AUTO_LOG_STACKS'],
        tags=app.settings['SENTRY_TAGS'],
        release=app.settings['SENTRY_RELEASE'],
        extra={
            'app': app,
        },
    )
