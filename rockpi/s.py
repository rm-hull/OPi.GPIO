# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for RockPi S board
(see https://wiki.radxa.com/RockpiS/hardware/gpio)

Usage:

.. code:: python
   import rockpi.s
   from OPi import GPIO

   GPIO.setmode(rockpi.s.BOARD)
"""

# Rock Pi S physical board pin to GPIO pin
BOARD = {
    0: 0,
    3: 11,
    5: 12,
    7: 68,
    8: 65,
    10: 64,
    11: 15,
    12: 69,
    13: 16,
    15: 17,
    16: 74,
    18: 73,
    19: 55,
    21: 54,
    22: 71,
    23: 56,
    24: 57,
    26: 0
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
