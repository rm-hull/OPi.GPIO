#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`OPi.event` module.
"""

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import time
import pytest
import OPi.event as event
from OPi.constants import RISING


def test_blocking_wait_for_edge_detected(fs):
    pin = 198
    fs.CreateFile("/sys/class/gpio/gpio{0}/edge".format(pin))
    fs.CreateFile("/sys/class/gpio/gpio{0}/value".format(pin))

    with patch("select.epoll") as mock:
        mock.return_value.poll.return_value = [(pin, 23)]
        assert event.blocking_wait_for_edge(pin, RISING, timeout=0.01) == pin


def test_blocking_wait_for_edge_timeout(fs):
    pin = 68
    fs.CreateFile("/sys/class/gpio/gpio{0}/edge".format(pin))
    fs.CreateFile("/sys/class/gpio/gpio{0}/value".format(pin))

    with patch("select.epoll"):
        assert event.blocking_wait_for_edge(pin, RISING, timeout=0.01) is None


def test_add_edge_callback_not_setup():
    pin = 32
    with pytest.raises(RuntimeError) as ex:
        event.add_edge_callback(pin, None)
    assert str(ex.value) == "Add event detection before adding a callback"


def test_event_detected_not_configured():
    pin = 54
    assert pin not in event._threads
    assert not event.edge_detected(pin)


def test_edge_detected(fs):
    pin = 23
    fs.CreateFile("/sys/class/gpio/gpio{0}/edge".format(pin))
    fs.CreateFile("/sys/class/gpio/gpio{0}/value".format(pin))

    with patch("select.epoll") as mock:
        try:
            assert pin not in event._threads
            event.add_edge_detect(pin, RISING)
            assert not event.edge_detected(pin)
            mock.return_value.poll.return_value = [(pin, 4)]
            time.sleep(2)
            event._threads[pin].cancel()
            assert event.edge_detected(pin)
            assert not event.edge_detected(pin)

        finally:
            event.cleanup()
            assert pin not in event._threads


def test_add_edge_detect_called_twice_throws_error(fs):
    pin = 43
    fs.CreateFile("/sys/class/gpio/gpio{0}/edge".format(pin))
    fs.CreateFile("/sys/class/gpio/gpio{0}/value".format(pin))

    with patch("select.epoll"):
        try:
            event.add_edge_detect(pin, RISING)
            assert pin in event._threads
            with pytest.raises(RuntimeError) as ex:
                event.add_edge_detect(pin, RISING)
            assert str(ex.value) == "Conflicting edge detection already enabled for this GPIO channel"

        finally:
            event.cleanup()
            assert pin not in event._threads


def test_blocking_wait_raises_error_add_edge_detect_already_active(fs):
    pin = 66
    fs.CreateFile("/sys/class/gpio/gpio{0}/edge".format(pin))
    fs.CreateFile("/sys/class/gpio/gpio{0}/value".format(pin))

    with patch("select.epoll"):
        try:
            assert pin not in event._threads
            event.add_edge_detect(pin, RISING)

            with pytest.raises(RuntimeError) as ex:
                event.blocking_wait_for_edge(pin, RISING)

            assert str(ex.value) == "Conflicting edge detection events already exist for this GPIO channel"

        finally:
            event.cleanup()


def test_callback_raises_error(fs):
    pin = 194
    fs.CreateFile("/sys/class/gpio/gpio{0}/edge".format(pin))
    fs.CreateFile("/sys/class/gpio/gpio{0}/value".format(pin))

    def cb(p):
        raise RuntimeError("test exception")

    with patch("select.epoll") as mock:
        try:
            assert pin not in event._threads
            event.add_edge_detect(pin, RISING, cb)
            mock.return_value.poll.return_value = [(pin, 74)]
            time.sleep(2)

            with pytest.raises(RuntimeError) as ex:
                event.cleanup(pin)

            assert str(ex.value) == "test exception"

        finally:
            event.cleanup()


def test_add_edge_callback(fs):
    pin = 71
    fs.CreateFile("/sys/class/gpio/gpio{0}/edge".format(pin))
    fs.CreateFile("/sys/class/gpio/gpio{0}/value".format(pin))

    called = {}

    def cb(p):
        called[p] = True

    with patch("select.epoll") as mock:
        try:
            assert pin not in event._threads
            event.add_edge_detect(pin, RISING)
            event.add_edge_callback(pin, cb)
            mock.return_value.poll.return_value = [(pin, 4)]
            time.sleep(2)
            event.cleanup(pin)
            assert pin in called

        finally:
            event.cleanup()
