# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Zero
(see https://linux-sunxi.org/images/e/e0/Orange-Pi-Zero-Schanetics-v1_11.pdf)

Usage:

.. code:: python
   import orangepi.zero
   from OPi import GPIO

   GPIO.setmode(orangepi.zero.BOARD) or GPIO.setmode(orangepi.zero.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.zeroplus

# Orange Pi Zero physical board pin to GPIO pin
BOARD = orangepi.zeroplus.BOARD

# Orange Pi Zero BCM pin to actual GPIO pin
BCM = orangepi.zeroplus.BCM
