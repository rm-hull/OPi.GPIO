# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI One
(see http://linux-sunxi.org/images/7/7e/ORANGE_PI-ONE-V1_1.pdf)

Usage:

.. code:: python
   import orangepi.one
   from OPi import GPIO

   GPIO.setmode(orangepi.one.BOARD) or GPIO.setmode(orangepi.one.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.pc

# Orange Pi One physical board pin to GPIO pin
BOARD = orangepi.pc.BOARD

# Orange Pi One BCM pin to actual GPIO pin
BCM = orangepi.pc.BCM
