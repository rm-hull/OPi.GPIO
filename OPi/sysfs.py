# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

from OPi.constants import HIGH, LOW, INPUT, OUTPUT
from OPi.pin_mappings import get_gpio_pin


def export(mode, pin):
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/export"
    with open(path, "w") as fp:
        fp.write(str(gpio))


def unexport(mode, pin):
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/unexport"
    with open(path, "w") as fp:
        fp.write(str(gpio))


def direction(mode, pin, dir):
    assert dir in [INPUT, OUTPUT]
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/gpio{0}/direction".format(gpio)
    with open(path, "w") as fp:
        if dir == INPUT:
            fp.write("in")
        else:
            fp.write("out")


def input(mode, pin):
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/gpio{0}/value".format(gpio)
    with open(path, "r") as fp:
        value = fp.read()
        if value.strip() == str(LOW):
            return LOW
        else:
            return HIGH


def output(mode, pin, value):
    assert value in [HIGH, LOW]
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/gpio{0}/value".format(gpio)
    with open(path, "w") as fp:
        fp.write(str(value))


#def edge(mode, pin, trigger):
#    assert trigger in [] # none, rising, falling, both
#    gpio = get_gpio_pin(mode, pin)
#    path = "/sys/class/gpio/gpio{0}/edge".format(gpio)
#    with open(path, "w") as fp:
#        fp.write("none")
#    with open(path, "w") as fp:
#        fp.write("none")
