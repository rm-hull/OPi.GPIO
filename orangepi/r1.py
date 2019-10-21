# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI R1
(see ORANGE_PI-R1-V1_1_Schematic.pdf document from Orange Pi Website
no direct link)

Usage:

.. code:: python
   import orangepi.r1
   from OPi import GPIO

   GPIO.setmode(orangepi.r1.BOARD) or GPIO.setmode(orangepi.r1.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.zeroplus

# Orange Pi R1 physical board pin to GPIO pin
BOARD = orangepi.zeroplus.BOARD

# Orange Pi R1 BCM pin to actual GPIO pin
BCM = orangepi.zeroplus.BCM
