# -*- coding: utf-8 -*-
# Copyright (c) 2025 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange Pi 5 Pro

Usage:

.. code:: python
   from OPi import GPIO
   from orangepi import pi5pro

   GPIO.setmode(pi5pro.BOARD)
"""

BOARD = {
    3:   59,   # GPIO1_D3 - UART4_RX_M0 / I2C1_SDA_M4
    5:   58,   # GPIO1_D2 - UART4_TX_M0 / I2C1_SCL_M4
    7:   47,   # GPIO1_B7 - UART1_RX_M1 / I2C5_SDA_M3 / PWM13_M2
    8:   13,   # GPIO0_B5 - UART2_TX_M0
    10:  14,   # GPIO0_B6 - UART2_RX_M0
    11: 138,   # GPIO4_B2 - PWM14_M1 / CAN1_RX_M1
    12:  39,   # GPIO1_A7 - PWM15_IR_M1
    13: 139,   # GPIO4_B3 - CAN1_TX_M1 / UART1_TX_M1
    15:  46,   # GPIO1_B6 - UART1_TX_M1 / I2C5_SCL_M3
    16:  33,   # GPIO1_A1 - UART4_RX_M2 / SPI0_MOSI_M2
    18:  32,   # GPIO1_A0 - UART6_RX_M1 / SPI4_MISO_M2
    19:  42,   # GPIO1_B2 - SPI0_MOSI_M2 / UART4_RX_M2 (overlap)
    21:  41,   # GPIO1_B1 - SPI0_MISO_M2 / UART6_RX_M1 (overlap)
    22:  40,   # GPIO1_B0 - SPI0_CLK_M2 / UART4_TX_M2
    23:  43,   # GPIO1_B3 - SPI0_CLK_M2 / UART4_TX_M2
    24:  44,   # GPIO1_B4 - SPI0_CS0_M2 / UART7_RX_M2
    26:  45,   # GPIO1_B5 - SPI0_CS1_M2 / UART7_TX_M2
    27:  34,   # GPIO1_A2 - I2C4_SDA_M3 / SPI4_CLK_M2
    28:  35,   # GPIO1_A3 - I2C4_SCL_M3 / PWM1_M2 / SPI4_CS0_M2
    29:  36,   # GPIO1_A4 - —
    31:  38,   # GPIO1_A6 - —
    32:  62,   # GPIO1_D6 - PWM14_M2 / I2C8_SCL_M2
    33:  63,   # GPIO1_D7 - I2C8_SDA_M2 / PWM15_IR_M3
    35: 135,   # GPIO4_A7 - I2C5_SDA_M2
    36: 131,   # GPIO4_A3 - UART0_TX_M2
    37: 134,   # GPIO4_A6 - I2C5_SCL_M2
    38: 132,   # GPIO4_A4 - UART0_RX_M2
    40: 133,   # GPIO4_A5 - UART3_TX_M2
}

# BCM alias
BCM = BOARD
