# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for NanoPi M4, M4B, and M4V2
(see http://wiki.friendlyarm.com/wiki/images/d/dd/NanoPi-M4-2GB-1807-Schematic.pdf)

Usage:

.. code:: python
   import nanopi.m4
   from OPi import GPIO

   GPIO.setmode(nanopi.m4.BOARD) or GPIO.setmode(nanopi.m4.BCM)
"""

# The Rockchip RK3399 GPIO has 5 banks, GPIO0 to GPIO4, each with 32 pins.
# Each bank is then divided into 4 parts with 8 pins each, labeled A through D (A=0, B=1, C=2, D=3)
# So, GPIO4_D5 is 4*32 + 3*8 + 5 = 157

# NanoPi M4 physical board pin to GPIO pin
BOARD = {
    7:    32,    # GPIO1_A0
    8:    145,   # GPIO4_C1/I2C3_SCL
    10:   144,   # GPIO4_C0/I2C3_SDA
    11:   33,    # GPIO1_A1
    12:   50,    # GPIO1_C2
    13:   35,    # GPIO1_A3
    15:   36,    # GPIO1_A4
    16:   54,    # GPIO1_C6
    18:   55,    # GPIO1_C7
    19:   40,    # GPIO1_B0/SPI1_TXD/UART4_TX
    21:   39,    # GPIO1_A7/SPI1_RXD/UART4_RX
    22:   56,    # GPIO1_D0
    23:   41,    # GPIO1_B1/SPI1_CLK
    24:   42,    # GPIO1_B2/SPI1_CSn0
    26:   149    # GPIO4_C5/SPDIF_TX
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
