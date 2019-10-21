# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Plus 2E
(see https://linux-sunxi.org/images/0/03/Orangepi-plus-2e-v1_1-schematic.pdf)

Usage:

.. code:: python
   import orangepi.plus2e
   from OPi import GPIO

   GPIO.setmode(orangepi.plus2e.BOARD) or GPIO.setmode(orangepi.plus2e.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.pc

# Orange Pi One physical board pin to GPIO pin
BOARD = orangepi.pc.BOARD

# Orange Pi One BCM pin to actual GPIO pin
BCM = orangepi.pc.BCM
