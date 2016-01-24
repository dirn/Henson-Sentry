"""Test configuration."""

import asyncio

from henson import Application
from raven.base import Client
import pytest

from henson_sentry import Sentry


class MockClient(Client):
    def __init__(self, *args, **kwargs):
        self._events = []
        super().__init__(*args, **kwargs)

    def is_enabled(self):
        return True

    def send(self, **kwargs):
        self._events.append(kwargs)


class MockConsumer:
    @asyncio.coroutine
    def read(self):
        return 1


@pytest.fixture
def cancelled_future(event_loop):
    """Return a Future that's been cancelled."""
    future = asyncio.Future(loop=event_loop)
    future.cancel()
    return future


@pytest.fixture
def queue():
    """Return a primed asynchronous queue."""
    queue = asyncio.Queue()
    queue.put_nowait(1)

    return queue


@pytest.fixture
def sentry(test_client, test_app):
    """Return an instance of the Sentry plugin."""
    sentry = Sentry()
    sentry._client = test_client
    sentry.init_app(test_app)

    return sentry


@pytest.fixture
def test_app(test_consumer, event_loop):
    """Return a test application."""
    @asyncio.coroutine
    def callback(app, message):
        raise Exception('testing')

    app = Application('testing', callback=callback, consumer=test_consumer)
    app.settings['SENTRY_DSN'] = 'testing'

    @app.message_acknowledgement
    @asyncio.coroutine
    def stop_loop(app, message):
        event_loop.stop()

    return app


@pytest.fixture
def test_client():
    """Return a mock client."""
    return MockClient()


@pytest.fixture
def test_consumer():
    """Return a mock consumer."""
    return MockConsumer()
