# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for NanoPi NEO Core2 board with/without Mini Shield
(see http://wiki.friendlyarm.com/wiki/index.php/NanoPi_NEO_Core2#Layout)

Usage:

.. code:: python
   import nanopi.neocore2
   from OPi import GPIO

   GPIO.setmode(nanopi.neocore2.BOARD) or GPIO.setmode(nanopi.neocore2.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PG11 is (7 - 1) * 32 + 11 = 203

# NanoPi NEO Core2 physical board pin to GPIO pin
BOARD = {
    3:   12,    # PA12/TWI0_SDA/DI_RX/PA_EINT12
    5:   11,    # PA11/TWI0_SCK/DI_TX/PA_EINT11
    7:  203,    # PG11/PCM1_CLK/PG_EINT11
    8:  198,    # PG6/UART1_TX/PG_EINT6
    10: 199,    # PG7/UART1_RX/PG_EINT7
    11:   0,    # PA0/UART2_TX/JTAG_MS0/PA_EINT0
    12:   6,    # PA6/SIM_PWREN/PWM1/PA_EINT6
    13:   2,    # PA2/UART2_RTS/JTAG_DO0/PA_EINT2
    15:   3,    # PA3/UART2_CTS/JTAG_DI0/PA_EINT3
    16: 200,    # PG8/UART1_RTS/PG_EINT8
    18: 201,    # PG9/UART1_CTS/PG_EINT9
    19:  64,    # PC0/NAND_WE/SPI0_MOSI
    21:  65,    # PC1/NAND_ALE/SPI0_MISO
    22:   1,    # PA1/UART2_RX/JTAG_CK0/PA_EINT1
    23:  66,    # PC2/NAND_CLE/SPI0_CLK
    24:  67     # PC3/NAND_CE1/SPI0_CS
}

# NanoPi NEO Core2 BCM pin to actual GPIO pin
BCM = {
    2:   12,    # PA12/TWI0_SDA/DI_RX/PA_EINT12
    3:   11,    # PA11/TWI0_SCK/DI_TX/PA_EINT11
    4:  203,    # PG11/PCM1_CLK/PG_EINT11
    8:   67,    # PC3/NAND_CE1/SPI0_CS
    9:   65,    # PC1/NAND_ALE/SPI0_MISO
    10:  64,    # PC0/NAND_WE/SPI0_MOSI
    11:  66,    # PC2/NAND_CLE/SPI0_CLK
    14: 198,    # PG6/UART1_TX/PG_EINT6
    15: 199,    # PG7/UART1_RX/PG_EINT7
    17:   0,    # PA0/UART2_TX/JTAG_MS0/PA_EINT0
    18:   6,    # PA6/SIM_PWREN/PWM1/PA_EINT6
    22:   3,    # PA3/UART2_CTS/JTAG_DI0/PA_EINT3
    23: 200,    # PG8/UART1_RTS/PG_EINT8
    24: 201,    # PG9/UART1_CTS/PG_EINT9
    25:   1,    # PA1/UART2_RX/JTAG_CK0/PA_EINT1
    27:   2     # PA2/UART2_RTS/JTAG_DO0/PA_EINT2
}
