# -*- coding: utf-8 -*-
# Copyright (c) 2022 sillo01
# See LICENSE.md for details.

"""
Usage:
.. code:: python
   import orangepi.zero2w
   from OPi import GPIO
   GPIO.setmode(orangepi.zero2w.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi Zero 2W physical board pin to GPIO pin
BOARD = {
    3:    232,   # PI8/TWI1_SDA
    5:    231,   # PI7/TWI1_SCL
    7:    237,   # PI13/PWM3/UART4_TX
    8:    192,   # PH0/UART0_TX
    10:   193,   # PH1/UART0_RX
    11:   194,   # PH2/UART5_TX
    12:   225,   # PI1
    13:   195,   # PH3/UART5_RX
    15:   229,   # PI5/TWI0_SCL/UART2_TX
    16:   238,   # PI14/PWM4/UART4_RX
    18:   196,   # PH4
    19:   199,   # PH7/SPI1_MOSI
    21:   200,   # PH8/SPI1_MISO
    22:   230,   # PI6/TWI0_SDA/UART2_RX
    23:   198,   # PH6/SPI1_CLK
    24:   197,   # PH5/SPI1_CS0
    26:   201,   # PH9/SPI1_CS1
    27:   234,   # PH10/TWI2_SDA/UART3_RX
    28:   233,   # PI9/TWI2_SCL/UART3_TX
    29:   224,   # PH0
    31:   239,   # PH15
    32:   235,   # PI11/PWM1
    33:   236,   # PI12/PWM2
    35:   226,   # PI2
    36:   44,    # PC12
    37:   240,   # PI16
    38:   228,   # PI4
    40:   227    # PI3
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD
