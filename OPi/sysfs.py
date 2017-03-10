#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

from OPi.constants import IN, OUT, HIGH, LOW
from OPi.pin_mapper import get_gpio_pin


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
    assert dir in [IN, OUT]
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/gpio{0}/direction".format(gpio)
    with open(path, "w") as fp:
        if dir == IN:
            fp.write("in")
        else:
            fp.write("out")


def input(mode, pin):
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/gpio{0}/value".format(gpio)
    with open(path, "r") as fp:
        return fp.read()


def output(mode, pin, value):
    assert value in [HIGH, LOW]
    gpio = get_gpio_pin(mode, pin)
    path = "/sys/class/gpio/gpio{0}/value".format(gpio)
    with open(path, "w") as fp:
        fp.write(str(value))
