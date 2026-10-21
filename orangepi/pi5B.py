# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 5B

Usage:

.. code:: python
   from orangepi import pi5B
   from OPi import GPIO

   GPIO.setmode(pi5B.BOARD) or GPIO.setmode(pi5B.BCM)
"""

from orangepi import pi5

# Orange Pi 5B physical board pin to GPIO pin
BOARD = pi5.BOARD

# No reason for BCM mapping, keeping it for compatibility
BCM = pi5.BCM
