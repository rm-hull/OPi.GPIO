# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 4
(https://drive.google.com/drive/folders/1jALhyhwjSVsxwSX1MwhjiOyQdx_fwlFg)

Usage:

.. code:: python
   import orangepi.4
   from OPi import GPIO

   GPIO.setmode(orangepi.4.BOARD) or GPIO.setmode(orangepi.4.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi 4 physical board pin to GPIO pin
BOARD = {
    3: 64,    # I2C2_SDA_3V0
    5: 65,    # I2C2_SCL_3V0
    7: 150,   # GPIO4_C6/PWM1
    8: 145,   # I2C3_SCL
    10: 144,  # I2C3_SDA
    11: 33,   # GPIO1_A1
    12: 50,   # GPIO1_C2
    13: 35,   # GPIO1_A3
    15: 92,   # GPIO2_D4
    16: 54,   # GPIO1_C6
    18: 55,   # GPIO1_C7
    19: 40,   # UART4_TX
    21: 39,   # UART4_RX
    22: 56,   # GPIO1_D0
    23: 41,   # SPI1_CLK
    24: 42,   # SPI1_CSn0
    26: 149,  # GPIO4_C5
    27: 64,   # I2C2_SDA
    28: 65,   # I2C2_SCL
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
