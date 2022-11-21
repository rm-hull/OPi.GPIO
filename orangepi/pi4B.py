# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 4B
(see https://drive.google.com/drive/folders/1jALhyhwjSVsxwSX1MwhjiOyQdx_fwlFg)

Usage:

.. code:: python
   import orangepi.pi4B
   from OPi import GPIO

   GPIO.setmode(orangepi.pi4B.BOARD) or GPIO.setmode(orangepi.pi4B.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

import orangepi.pi4B

# Orange Pi One physical board pin to GPIO pin
BOARD = orangepi.pi4B.BOARD

# Orange Pi One BCM pin to actual GPIO pin
BCM = orangepi.pi4B.BCM
