# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Prime
(see http://linux-sunxi.org/images/a/ae/ORANGEPI-Prime_V1_0.pdf)

Usage:

.. code:: python
   import orangepi.prime
   from OPi import GPIO

   GPIO.setmode(orangepi.prime.BOARD) or GPIO.setmode(orangepi.prime.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.pc

# Orange Pi One physical board pin to GPIO pin
BOARD = orangepi.pc.BOARD

# Orange Pi One BCM pin to actual GPIO pin
BCM = orangepi.pc.BCM
