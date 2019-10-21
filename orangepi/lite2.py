# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Lite 2
(see http://linux-sunxi.org/images/4/4c/OrangePi_Lite2_Schematics_v2.0.pdf)

Usage:

.. code:: python
   import orangepi.lite2
   from OPi import GPIO

   GPIO.setmode(orangepi.lite2.BOARD) or GPIO.setmode(orangepi.lite2.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.oneplus

# Orange Pi Lite 2 physical board pin to GPIO pin
BOARD = orangepi.oneplus.BOARD

# Orange Pi Lite 2 BCM pin to actual GPIO pin
BCM = orangepi.oneplus.BCM
