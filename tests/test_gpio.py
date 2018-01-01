#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`OPi.GPIO` module.
"""
try:
    from unittest.mock import patch, call
except ImportError:
    from mock import patch, call

import pytest
import OPi.GPIO as GPIO


def setup():
    with patch("OPi.GPIO.sysfs"):
        GPIO.cleanup()


def test_mode():
    assert GPIO.getmode() is None
    GPIO.setmode(GPIO.BCM)
    assert GPIO.getmode() == GPIO.BCM
    GPIO.cleanup()
    assert GPIO.getmode() is None
    with pytest.raises(AssertionError):
        GPIO.setmode(54335)


def test_warnings():
    GPIO.setwarnings(False)
    assert not GPIO._gpio_warnings
    GPIO.setwarnings(True)
    assert GPIO._gpio_warnings


def test_setup_with_no_mode():
    with pytest.raises(RuntimeError) as ex:
        GPIO.setup(3, GPIO.IN)
    assert str(ex.value) == "Mode has not been set"


def test_setup_single_input_channel():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.SUNXI)
        GPIO.setup("PA01", GPIO.IN)
        mock.export.assert_called_with(1)
        mock.direction.assert_called_with(1, GPIO.IN)
        assert "PA01" in GPIO._exports


def test_setup_channel_already_setup():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.SUNXI)
        GPIO.setup("PA01", GPIO.IN)
        mock.export.assert_called_with(1)
        mock.direction.assert_called_with(1, GPIO.IN)
        assert "PA01" in GPIO._exports
        with pytest.raises(RuntimeError) as ex:
            GPIO.setup("PA01", GPIO.OUT)
        assert str(ex.value) == "Channel PA01 is already configured"


def test_setup_single_output_channel():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.SUNXI)
        GPIO.setup("PG07", GPIO.OUT)
        mock.export.assert_called_with(199)
        mock.direction.assert_called_with(199, GPIO.OUT)
        mock.output.assert_not_called()
        assert "PG07" in GPIO._exports


def test_setup_channel_already_in_use_raises_OSError():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.SUNXI)
        mock.export.side_effect = [OSError(16, "test"), None]
        GPIO.setup("PG07", GPIO.OUT)
        mock.export.assert_called_with(199)
        mock.unexport.assert_called_with(199)
        mock.direction.assert_called_with(199, GPIO.OUT)
        mock.output.assert_not_called()
        assert "PG07" in GPIO._exports


def test_setup_channel_already_in_use_raises_IOError():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.SUNXI)
        mock.export.side_effect = [IOError(16, "test"), None]
        GPIO.setup("PG06", GPIO.OUT)
        mock.export.assert_called_with(198)
        mock.unexport.assert_called_with(198)
        mock.direction.assert_called_with(198, GPIO.OUT)
        mock.output.assert_not_called()
        assert "PG06" in GPIO._exports


def test_setup_raises_OSError():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.SUNXI)
        mock.export.side_effect = OSError(44, "test")
        with pytest.raises(OSError) as ex:
            GPIO.setup("PG07", GPIO.OUT)
        assert str(ex.value) == "[Errno 44] test"
        mock.export.assert_called_with(199)
        mock.unexport.assert_not_called()
        mock.direction.assert_not_called()
        mock.output.assert_not_called()
        assert "PG07" not in GPIO._exports


def test_setup_single_output_channel_with_initial_value():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.SUNXI)
        GPIO.setup("PG06", GPIO.OUT, GPIO.HIGH)
        mock.export.assert_called_with(198)
        mock.direction.assert_called_with(198, GPIO.OUT)
        mock.output.assert_called_with(198, GPIO.HIGH)
        assert "PG06" in GPIO._exports


def test_input_not_configured():
    with pytest.raises(RuntimeError) as ex:
        GPIO.input(12)
    assert str(ex.value) == "Channel 12 is not configured"


def test_input():
    with patch("OPi.GPIO.sysfs") as mock:
        mock.input.return_value = GPIO.HIGH
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.IN)
        assert GPIO.input(23) == GPIO.HIGH
        mock.input.assert_called_with(14)


def test_input_not_configured_for_output():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.IN)
        with pytest.raises(RuntimeError) as ex:
            GPIO.output(23, GPIO.LOW)
        assert str(ex.value) == "Channel 23 is configured for input"


def test_output_not_configured():
    with pytest.raises(RuntimeError) as ex:
        GPIO.output(12, GPIO.LOW)
    assert str(ex.value) == "Channel 12 is not configured"


def test_output():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.OUT)
        GPIO.output(23, GPIO.LOW)
        mock.output.assert_called_with(14, GPIO.LOW)


def test_multiple_output():
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([23, 13, 3], GPIO.OUT)
        GPIO.output([23, 13, 3], GPIO.LOW)
        mock.output.assert_has_calls([
            call(14, GPIO.LOW),
            call(0, GPIO.LOW),
            call(12, GPIO.LOW)
        ])


def test_input_and_output():
    with patch("OPi.GPIO.sysfs") as mock:
        mock.input.return_value = GPIO.HIGH
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.OUT)
        GPIO.output(23, not GPIO.input(23))
        mock.input.assert_called_with(14)
        mock.output.assert_called_with(14, GPIO.LOW)


def test_wait_for_edge_not_configured():
    with pytest.raises(RuntimeError) as ex:
        GPIO.wait_for_edge(91, GPIO.RISING)
    assert str(ex.value) == "Channel 91 is not configured"


def test_wait_for_edge_not_configured_for_input():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.OUT)
        with pytest.raises(RuntimeError) as ex:
            GPIO.wait_for_edge(12, GPIO.RISING)
        assert str(ex.value) == "Channel 12 is configured for output"


def test_wait_for_edge_completes():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.IN)
        with patch("OPi.GPIO.event") as mock:
            mock.blocking_wait_for_edge.return_value = 1
            assert GPIO.wait_for_edge(12, GPIO.BOTH) == 12
            mock.blocking_wait_for_edge.assert_called_with(7, GPIO.BOTH, -1)


def test_add_event_detect():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.IN)
        with patch("OPi.GPIO.event") as mock:
            GPIO.add_event_detect(23, GPIO.BOTH)
            mock.add_edge_detect.assert_called_with(14, GPIO.BOTH, None)


def test_add_event_detect_not_configured_for_input():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.OUT)
        with pytest.raises(RuntimeError) as ex:
            GPIO.add_event_detect(23, GPIO.FALLING)
        assert str(ex.value) == "Channel 23 is configured for output"


def test_remove_event_detect():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.IN)
        with patch("OPi.GPIO.event") as mock:
            GPIO.remove_event_detect(23)
            mock.remove_edge_detect.assert_called_with(14)


def test_remove_event_detect_not_configured_for_input():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.OUT)
        with pytest.raises(RuntimeError) as ex:
            GPIO.remove_event_detect(23)
        assert str(ex.value) == "Channel 23 is configured for output"


def test_add_event_callback():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.IN)
        with patch("OPi.GPIO.event") as mock:
            GPIO.add_event_callback(23, None)
            mock.add_edge_callback(14, None)


def test_add_event_callback_not_configured_for_input():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.OUT)
        with pytest.raises(RuntimeError) as ex:
            GPIO.add_event_callback(23, None)
        assert str(ex.value) == "Channel 23 is configured for output"


def test_event_detected():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.IN)
        with patch("OPi.GPIO.event") as mock:
            mock.edge_detected.return_value = True
            assert GPIO.event_detected(23)


def test_event_detected_not_configured_for_input():
    with patch("OPi.GPIO.sysfs"):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(23, GPIO.OUT)
        with pytest.raises(RuntimeError) as ex:
            GPIO.event_detected(23)
        assert str(ex.value) == "Channel 23 is configured for output"


def test_callback_wrapper_none():
    assert GPIO.__wrap(None, 12) is None


def test_callback_wrapper_not_none():
    called = []

    def cb(pin):
        called.append(pin)

    callback = GPIO.__wrap(cb, 17)
    callback(97)
    assert 17 in called
    assert 97 not in called


def test_custom_dict():
    GPIO.cleanup()
    assert GPIO.getmode() is None
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode({"A": 5, "B": 37})
        assert GPIO.getmode() is GPIO.CUSTOM
        GPIO.setup("A", GPIO.IN)
        mock.export.assert_called_with(5)
        mock.direction.assert_called_with(5, GPIO.IN)
        assert "A" in GPIO._exports


def test_custom_object():
    class mapper(object):
        def __getitem__(self, value):
            return value + 4

    GPIO.cleanup()
    assert GPIO.getmode() is None
    with patch("OPi.GPIO.sysfs") as mock:
        GPIO.setmode(mapper())
        assert GPIO.getmode() is GPIO.CUSTOM
        GPIO.setup(11, GPIO.IN)
        mock.export.assert_called_with(15)
        mock.direction.assert_called_with(15, GPIO.IN)
        assert 11 in GPIO._exports
