"""Test Henson-Sentry."""

import asyncio

from henson_sentry import Sentry


def test_capture_exception(sentry, test_app, event_loop, cancelled_future,
                           queue):
    """Test capture_exception."""
    @asyncio.coroutine
    def callback(app, message):
        try:
            1 / 0
        except:
            yield from sentry.capture_exception()
    test_app.callback = callback

    event_loop.run_until_complete(
        test_app._process(cancelled_future, queue, event_loop))

    assert sentry._client._events


def test_capture_message(sentry, test_app, event_loop, cancelled_future,
                         queue):
    """Test capture_message."""
    @asyncio.coroutine
    def callback(app, message):
        yield from sentry.capture_message(message)
    test_app.callback = callback

    event_loop.run_until_complete(
        test_app._process(cancelled_future, queue, event_loop))

    assert sentry._client._events


def test_handle_exception(sentry, test_app, event_loop, cancelled_future,
                          queue):
    """Test that exceptions are handled."""
    event_loop.run_until_complete(
        test_app._process(cancelled_future, queue, event_loop))

    assert sentry._client._events


def test_handle_exception_with_ignored_error(sentry, test_app, event_loop,
                                             cancelled_future, queue):
    """Test that ignored exceptions aren't handled."""
    test_app.settings['RAVEN_IGNORE_EXCEPTIONS'] = Exception

    event_loop.run_until_complete(
        test_app._process(cancelled_future, queue, event_loop))

    assert not sentry._client._events


def test_no_dsn(test_app):
    """Test that Sentry is disabled when there's no DSN."""
    # Ensure that there's no DSN set for test_app.
    del test_app.settings['SENTRY_DSN']

    sentry = Sentry(test_app)

    assert sentry._client is None
