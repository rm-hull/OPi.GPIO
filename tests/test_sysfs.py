#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`OPi.sysfs` module.
"""

from OPi.sysfs import export, unexport, direction, input, output
from OPi.constants import INPUT, OUTPUT, LOW, HIGH


def test_export(fs):
    fs.CreateFile("/sys/class/gpio/export")
    export(19)
    with open("/sys/class/gpio/export") as fp:
        assert fp.read() == "19"


def test_unexport(fs):
    fs.CreateFile("/sys/class/gpio/unexport")
    unexport(26)
    with open("/sys/class/gpio/unexport") as fp:
        assert fp.read() == "26"


def test_direction_input(fs):
    fs.CreateFile("/sys/class/gpio/gpio198/direction")
    direction(198, INPUT)
    with open("/sys/class/gpio/gpio198/direction") as fp:
        assert fp.read() == "in"


def test_direction_output(fs):
    fs.CreateFile("/sys/class/gpio/gpio199/direction")
    direction(199, OUTPUT)
    with open("/sys/class/gpio/gpio199/direction") as fp:
        assert fp.read() == "out"


def test_input_low(fs):
    fs.CreateFile("/sys/class/gpio/gpio0/value")
    with open("/sys/class/gpio/gpio0/value", "w") as fp:
        fp.write("0\n")
    assert input(0) == LOW


def test_input_high(fs):
    fs.CreateFile("/sys/class/gpio/gpio17/value")
    with open("/sys/class/gpio/gpio17/value", "w") as fp:
        fp.write("1\n")
    assert input(17) == HIGH


def test_output_low(fs):
    fs.CreateFile("/sys/class/gpio/gpio21/value")
    output(21, LOW)
    with open("/sys/class/gpio/gpio21/value") as fp:
        assert fp.read() == "0"


def test_output_high(fs):
    fs.CreateFile("/sys/class/gpio/gpio15/value")
    output(15, HIGH)
    with open("/sys/class/gpio/gpio15/value") as fp:
        assert fp.read() == "1"
