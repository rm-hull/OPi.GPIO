# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI PC Plus
(see orange_pi-pc_plus_v1_1 schemetic.pdf document from Orange Pi Website
no direct link)

Usage:

.. code:: python
   import orangepi.pcplus
   from OPi import GPIO

   GPIO.setmode(orangepi.pcplus.BOARD) or GPIO.setmode(orangepi.pcplus.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.pc

# Orange Pi PC Plus physical board pin to GPIO pin
BOARD = orangepi.pc.BOARD

# Orange Pi PC Plus BCM pin to actual GPIO pin
BCM = orangepi.pc.BCM
