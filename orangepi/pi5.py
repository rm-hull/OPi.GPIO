# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 5

Usage:

.. code:: python
   from orangepi import pi5
   from OPi import GPIO

   GPIO.setmode(pi5.BOARD) or GPIO.setmode(pi5.BCM)
"""

# Orange Pi 5B physical board pin to GPIO pin
BOARD = {
    3: 47,    # GPIO1_B7 PWM13_M2 UART1_RX_M1 I2C5_SDA_M3
    5: 46,    # GPIO1_B6 UART1_TX_M1 I2C5_SCL_M3
    7: 54,    # GPIO1_C6 PWM15_IR_M2
    8: 131,   # GPIO4_A3 UART0_TX_M2
    10: 132,  # GPIO4_A4 UART0_RX_M2
    11: 138,  # GPIO4_B2 PWM14_M1 CAN1_RX_M1
    12: 29,   # GPIO0_D5 CAN2_TX_M1
    13: 139,  # GPIO4_B3 CAN1_TX_M1
    15: 28,   # GPIO0_D4 PWM3_IR_M0 CAN2_RX_M1
    16: 59,   # GPIO1_D3 UART4_RX_M0 I2C1_SDA_M4
    18: 58,   # GPIO1_D2 UART4_TX_M0 I2C1_SCL_M4 PWM0_M1
    19: 49,   # GPIO1_C1 I2C3_SCL_M0 UART3_TX_M0 SPI4_MOSI_M0
    21: 48,   # GPIO1_C0 I2C3_SDA_M0 UART3_RX_M0 SPI4_MISO_M0
    22: 92,   # GPIO2_D4
    23: 50,   # GPIO1_C2 SPI4_CLK_M0
    24: 52,   # GPIO1_C4 SPI4_CS1_M0
    26: 35,   # GPIO1_A3 PWM1_M2
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
