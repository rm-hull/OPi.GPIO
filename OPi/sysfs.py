# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

from contextlib import contextmanager
from OPi.constants import HIGH, LOW, IN, OUT, \
    NONE, RISING, FALLING, BOTH


@contextmanager
def value_descriptor(pin, mode="r"):
    path = "/sys/class/gpio/gpio{0}/value".format(pin)
    with open(path, mode) as fp:
        yield fp


def export(pin):
    path = "/sys/class/gpio/export"
    with open(path, "w") as fp:
        fp.write(str(pin))


def unexport(pin):
    path = "/sys/class/gpio/unexport"
    with open(path, "w") as fp:
        fp.write(str(pin))


def direction(pin, dir):
    assert dir in [IN, OUT]
    path = "/sys/class/gpio/gpio{0}/direction".format(pin)
    with open(path, "w") as fp:
        if dir == IN:
            fp.write("in")
        else:
            fp.write("out")


def input(pin):
    with value_descriptor(pin) as fp:
        value = fp.read()
        if value.strip() == str(LOW):
            return LOW
        else:
            return HIGH


def output(pin, value):
    assert value in [HIGH, LOW]
    with value_descriptor(pin, "w") as fp:
        fp.write(str(value))


def edge(pin, trigger):
    assert trigger in [NONE, RISING, FALLING, BOTH]
    path = "/sys/class/gpio/gpio{0}/edge".format(pin)
    opts = {
        NONE: "none",
        RISING: "rising",
        FALLING: "falling",
        BOTH: "both"
    }
    with open(path, "w") as fp:
        fp.write(opts[trigger])
