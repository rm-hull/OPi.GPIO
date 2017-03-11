# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

from OPi.constants import HIGH, LOW, BCM, BOARD, SUNXI, INPUT, OUTPUT  # noqa: F401
from OPi.pin_mappings import get_gpio_pin
from OPi import sysfs

_mode = None
_exports = []


def _check_configured(channel):
    if channel not in _exports:
        raise RuntimeError("Channel {0} is not configured".format(channel))


def getmode():
    return _mode


def setmode(value):
    global _mode
    assert value in [BCM, BOARD, SUNXI]
    _mode = value


def setwarnings(enabled):
    pass


def setup(channel, direction, initial=LOW, pull_up_down=None):
    if isinstance(channel, list):
        for ch in channel:
            setup(ch, direction, initial, pull_up_down)
    else:
        if channel in _exports:
            raise RuntimeError("Channel {0} is already configured".format(channel))
        pin = get_gpio_pin(_mode, channel)
        sysfs.export(pin)
        sysfs.direction(pin, direction)
        if direction == OUTPUT:
            sysfs.output(pin, initial)

        _exports.append(channel)


def input(channel):
    _check_configured(channel)
    pin = get_gpio_pin(_mode, channel)
    return sysfs.input(pin)


def output(channel, state):
    if isinstance(channel, list):
        for ch in channel:
            output(ch, state)
    else:
        _check_configured(channel)
        pin = get_gpio_pin(_mode, channel)
        return sysfs.output(pin, state)


def cleanup(channel=None):
    if channel is None:
        cleanup(_exports)
    elif isinstance(channel, list):
        for ch in channel:
            cleanup(ch)
    else:
        _check_configured(channel)
        pin = get_gpio_pin(_mode, channel)
        sysfs.unexport(pin)
        _exports.remove(channel)
