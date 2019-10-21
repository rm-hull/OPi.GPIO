# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI One Plus
(https://linux-sunxi.org/images/7/7c/OrangePi_OnePlus_Schematics_v2.0.pdf)

Usage:

.. code:: python
   import orangepi.oneplus
   from OPi import GPIO

   GPIO.setmode(orangepi.oneplus.BOARD) or GPIO.setmode(orangepi.oneplus.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi One Plus physical board pin to GPIO pin
BOARD = {
    3:  230,    # PH6/SPI1-MISO/SPDIF-IN/TWI1-SDA/SIM1-DET
    5:  229,    # PH5/SPI1-MOSI/SPDIF-MCLK/TWI1-SCK/SIM1-RST
    7:  228,    # PH4/SPI1-CLK/PCM0-MCLK/H-PCM0-MCLK/SIM1-DATA/PWM1
    8:  117,    # PD21/LCD0-VSYNC/TS2-D0/UART2-RTS
    10: 118,    # PD22/PWM0/TS3-CLK/UART2-CTS
    11: 120,    # PD24/TWI2-SDA/TS3-SYNC/UART3-RX/JTAG-CK
    12:  73,    # PC9/NAND-DQ3/SDC2-D3
    13: 119,    # PD23/TWI2-SCK/TS3-ERR/UART3-TX/JTAG-MS
    15: 122,    # PD26/TWI0-SDA/TS3-D0/UART3-CTS/JTAG-DI
    16:  72,    # PC8/NAND-DQ2/SDC2-D2
    18:  71,    # PC7/NAND-DQ1/SDC2-D1/SPI0-WP
    19:  66,    # PC2/NAND-CLE/SPI0-MOSI
    21:  67,    # PC3/NAND-CE0/SPI0-MISO
    22: 121,    # PD25/TWI0-SCK/TS3-DVLD/UART3-RTS/JTAG-DO
    23:  64,    # PC0/NAND-WE/SPI0-CLK
    24:  69,    # PC5/NAND-RB0/SDC2-CMD/SPI0-CS
    26: 227     # PH3/SPI1-CS/PCM0-DIN/H-PCM0-DIN/SIM1-CLK
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
