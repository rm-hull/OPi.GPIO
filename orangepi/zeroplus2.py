# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Zero Plus2
(see http://linux-sunxi.org/File:ORANGE_PI-ZERO-PLUS2_V1_0.pdf)

Usage:

.. code:: python
   import orangepi.zeroplus2
   from OPi import GPIO

   GPIO.setmode(orangepi.zeroplus2.BOARD) or GPIO.setmode(orangepi.zeroplus2.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi Zero Plus2 physical board pin to GPIO pin
BOARD = {
    3:   12,    # PA12/TWI0_SDA/DI_RX/PA_EINT12
    5:   11,    # PA11/TWI0_SCK/DI_TX/PA_EINT11
    7:    6,    # PA6/SIM_PWREN/PWM1/PA_EINT6
    8:    0,    # PA0/UART2_TX/JTAG_MS0/PA_EINT0
    10:   1,    # PA1/UART2_RX/JTAG_CK/PA_EINT1
    11: 352,    # PL0/S_TWI_SCK/S_PL_EINT0
    12: 107,    # PD11/RGMII_NULL/MII_CRS/RMII_NULL
    13: 353,    # PL1/S_TWI_SDA/S_PL_EINT1
    15:   3,    # PA3/UART2_CTS/JTAG_DI/PA_EINT3
    16:  19,    # PA19/PCM0_CLK/TWI1_SDA/PA_EINT19
    18:  18,    # PA18/PCM0_SYNC/TWI1_SCK/PA_EINT18
    19:  15,    # PA15/SPI1_MOSI/UART3_RTS/PA_EINT15
    21:  16,    # PA16/SPI1_MISO/UART3_CTS/PA_EINT16
    22:   2,    # PA2/UART2_RTS/JTAG_DO/PA_EINT2
    23:  14,    # PA14/SPI1_CLK/UART3_RX/PA_EINT14
    24:  13,    # PA13/SPI1_CS/UART3_TX/PA_EINT13
    26: 110     # PD14/RGMII_NULL/MII_TXERR/RMII_NULL
}

# Orange Pi Zero Plus2 BCM pin to actual GPIO pin
BCM = {
    2:   12,    # PA12/TWI0_SDA/DI_RX/PA_EINT12
    3:   11,    # PA11/TWI0_SCK/DI_TX/PA_EINT11
    4:    6,    # PA6/SIM_PWREN/PWM1/PA_EINT6
    7:  110,    # PD14/RGMII_NULL/MII_TXERR/RMII_NULL
    8:   13,    # PA13/SPI1_CS/UART3_TX/PA_EINT13
    9:   16,    # PA16/SPI1_MISO/UART3_CTS/PA_EINT16
    10:  15,    # PA15/SPI1_MOSI/UART3_RTS/PA_EINT15
    11:  14,    # PA14/SPI1_CLK/UART3_RX/PA_EINT14
    14:   0,    # PA0/UART2_TX/JTAG_MS0/PA_EINT0
    15:   1,    # PA1/UART2_RX/JTAG_CK/PA_EINT1
    17: 352,    # PL0/S_TWI_SCK/S_PL_EINT0
    18: 107,    # PD11/RGMII_NULL/MII_CRS/RMII_NULL
    22:   3,    # PA3/UART2_CTS/JTAG_DI/PA_EINT3
    23:  19,    # PA19/PCM0_CLK/TWI1_SDA/PA_EINT19
    24:  18,    # PA18/PCM0_SYNC/TWI1_SCK/PA_EINT18
    25:   2,    # PA2/UART2_RTS/JTAG_DO/PA_EINT2
    27: 353     # PL1/S_TWI_SDA/S_PL_EINT1
}
