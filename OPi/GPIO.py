# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

from OPi.constants import HIGH, LOW, BCM, BOARD, SUNXI, INPUT, OUTPUT
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
        sysfs.export(_mode, channel)
        sysfs.direction(_mode, channel, direction)
        if direction == OUTPUT:
            sysfs.output(_mode, channel, initial)

        _exports.append(channel)


def input(channel):
    _check_configured(channel)
    return sysfs.input(_mode, channel)


def output(channel, state):
    if isinstance(channel, list):
        for ch in channel:
            output(ch, state)
    else:
        _check_configured(channel)
        return sysfs.output(_mode, channel, state)


def cleanup(channel=None):
    if channel is None:
        cleanup(_exports)
    elif isinstance(channel, list):
        for ch in channel:
            cleanup(ch)
    else:
        _check_configured(channel)
        sysfs.unexport(_mode, channel)
        _exports.remove(channel)
