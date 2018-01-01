# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.md for details.

import sys


class _const:

    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value


GPIO = _const()

# From: https://sourceforge.net/p/raspberry-gpio-python/code/ci/default/tree/source/c_gpio.h#l42
GPIO.IN = 1
GPIO.OUT = 0
GPIO.ALT0 = 4

GPIO.HIGH = 1
GPIO.LOW = 0

GPIO.PUD_OFF = 0
GPIO.PUD_DOWN = 1
GPIO.PUD_UP = 2

# From: https://sourceforge.net/p/raspberry-gpio-python/code/ci/default/tree/source/common.h
GPIO.BOARD = 10
GPIO.BCM = 11
GPIO.SUNXI = 12  # made up :]
GPIO.CUSTOM = 13  # also made up 8]

GPIO.NONE = 0
GPIO.RISING = 1
GPIO.FALLING = 2
GPIO.BOTH = 3

sys.modules[__name__] = GPIO
