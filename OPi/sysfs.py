# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

from OPi.constants import HIGH, LOW, INPUT, OUTPUT


def export(pin):
    path = "/sys/class/gpio/export"
    with open(path, "w") as fp:
        fp.write(str(pin))


def unexport(pin):
    path = "/sys/class/gpio/unexport"
    with open(path, "w") as fp:
        fp.write(str(pin))


def direction(pin, dir):
    assert dir in [INPUT, OUTPUT]
    path = "/sys/class/gpio/gpio{0}/direction".format(pin)
    with open(path, "w") as fp:
        if dir == INPUT:
            fp.write("in")
        else:
            fp.write("out")


def input(pin):
    path = "/sys/class/gpio/gpio{0}/value".format(pin)
    with open(path, "r") as fp:
        value = fp.read()
        if value.strip() == str(LOW):
            return LOW
        else:
            return HIGH


def output(pin, value):
    assert value in [HIGH, LOW]
    path = "/sys/class/gpio/gpio{0}/value".format(pin)
    with open(path, "w") as fp:
        fp.write(str(value))


# def edge(pin, trigger):
#    assert trigger in [] # none, rising, falling, both
#    path = "/sys/class/gpio/gpio{0}/edge".format(pin)
#    with open(path, "w") as fp:
#        fp.write("none")
#    with open(path, "w") as fp:
#        fp.write("none")
