# -*- coding: utf-8 -*-
# Copyright (c) 2022 T-REX-XP & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa Zero board
(see https://wiki.radxa.com/Zero/hardware/gpio)

Usage:

.. code:: python
   import radxazero.s
   from OPi import GPIO

   GPIO.setmode(radxazero.s.BOARD)
"""

# Rock Pi S physical board pin to GPIO pin
BOARD = {
   3:  490, #F2: I2C_EE_M3_SDA	F1: GPIOA_14
   5:  491, #F2: I2C_EE_M3_SCL	F1: GPIOA_15
   7:  415, #F4: I2C_AO_S0_SDA	F3: UART_AO_B_RX  F2: I2C_AO_M0_SDA	 F1:GPIOAO_3
   8:  412, #F1: GPIOAO_0   F2: UART_AO_A_TXD
   10: 413, #F1: GPIOAO_1   F2: UART_AO_A_RXD
   11: 414,
   12: 501,
   13: 503,
   16: 502,
   18: 500,
   19: 447,
   21: 448,
   22: 475,
   23: 450,
   24: 449,
   27: 415,
   28: 414,
   32: 416,
   35: 420,
   36: 451,
   37: 421,
   38: 422,
   40: 423
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
