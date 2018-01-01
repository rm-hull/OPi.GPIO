# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for NanoPi DUO board with/without Mini Shield (see
http://wiki.friendlyarm.com/wiki/index.php/NanoPi_Duo#Layout)

Usage:

.. code:: python
   import nanopi.duo
   from OPi import GPIO

   GPIO.setmode(nanopi.duo.BOARD)
"""

BOARD = {
    3: 12,  # I2C0_SDA/GPIOA12
    5: 11,  # I2C0_SCL/GPIOA11
    7: 203,  # GPIOG11
    8: 198,  # UART1_TX/GPIOG6
    10: 199,  # UART1_RX/GPIOG7
    11: 5,  # DEBUG_RX(UART_RXD0)/GPIOA5/PWM0
    12: 363,  # GPIOL11/IR-RX
    13: 4,  # DEBUG_TX(UART_TXD0)/GPIOA4
    19: 15,  # UART3_RTS/SPI1_MOSI/GPIOA15
    21: 16,  # UART3_CTS/SPI1_MISO/GPIOA16
    23: 14,  # UART3_RX/SPI1_CLK/GPIOA14
    24: 13,  # UART3_TX/SPI1_CS/GPIOA13
    41: 355  # Button
}

# NanoPi Duo BCM pin to actual GPIO pin
BCM = {
    2: 12,  # I2C0_SDA/GPIOA12
    3: 11,  # I2C0_SCL/GPIOA11
    4: 203,  # GPIOG11
    8: 13,  # UART3_TX/SPI1_CS/GPIOA13
    9: 16,  # UART3_CTS/SPI1_MISO/GPIOA16
    10: 15,  # UART3_RTS/SPI1_MOSI/GPIOA15
    11: 14,  # UART3_RX/SPI1_CLK/GPIOA14
    14: 198,  # UART1_TX/GPIOG6
    15: 199,  # UART1_RX/GPIOG7
    17: 5,  # DEBUG_RX(UART_RXD0)/GPIOA5/PWM0
    18: 363,  # GPIOL11/IR-RX
    27: 4,  # DEBUG_TX(UART_TXD0)/GPIOA4
    41: 355  # Button
}
