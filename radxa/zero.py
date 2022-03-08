# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa Zero
(see https://wiki.radxa.com/Zero/hardware/gpio)

Usage:

.. code:: python
   import radxa.zero
   from OPi import GPIO

   GPIO.setmode(radxa.zero.BOARD) or GPIO.setmode(radxa.zero.BCM)
"""

# Amlogic S905Y2 GPIOs are grouped in two banks, GPIO AO domain and GPIO EE domain
#     AO domain: GPIOAO_0 - GPIOAO_11
#     EE domain: GPIOA_14 - GPIOA_15 | GPIOH_0 - GPIOH_8 | GPIOX_0 - GPIOX_19

# ╔═════════════╦═════════════╦════════╦══════════╦═════════════════╗
# ║  GPIO Chip  ║  GPIO Name  ║  Base  ║  Offset  ║  Formula        ║
# ╠═════════════╬═════════════╬════════╬══════════╬═════════════════╣
# ║  First      ║  GPIOAO_x   ║  412   ║  0-11    ║  Base + Offset  ║
# ║  First      ║  GPIOE_x    ║  424   ║  0-2     ║  Base + Offset  ║
# ║  Second     ║  GPIOZ_x    ║  427   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOH_x    ║  443   ║  0-8     ║  Base + Offset  ║
# ║  Second     ║  BOOT_x     ║  452   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOC_x    ║  468   ║  0-7     ║  Base + Offset  ║
# ║  Second     ║  GPIOA_x    ║  476   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOX_x    ║  492   ║  0-19    ║  Base + Offset  ║
# ╚═════════════╩═════════════╩════════╩══════════╩═════════════════╝

# Radxa Zero physical board pin to GPIO pin
BOARD = {
    3:      490,    # GPIOA_14  | I2C_EE_M3_SDA
    5:      491,    # GPIOA_15  | I2C_EE_M3_SCL
    7:      415,    # GPIOAO_3  | I2C_AO_M0_SDA | UART_AO_B_RX  | I2C_AO_S0_SDA
    11:     414,    # GPIOAO_2  | I2C_AO_M0_SCL | UART_AO_B_TX  | I2C_AO_S0_SCL
    13:     503,    # GPIOX_11  | SPI_A_SCLK    | I2C_EE_M1_SCL
    19:     447,    # GPIOH_4   | UART_EE_C_RTS | SPI_B_MOSI
    21:     448,    # GPIOH_5   | UART_EE_C_CTS | SPI_B_MISO    | PWM_F
    23:     450,    # GPIOH_7   | UART_EE_C_TX  | SPI_B_SCLK    | I2C_EE_M1_SCL
    27:     415,    # GPIOAO_3  | I2C_AO_M0_SDA | UART_AO_B_RX  | I2C_AO_S0_SDA
    35:     420,    # GPIOAO_8  | UART_AO_B_TX
    37:     421,    # GPIOAO_9  | UART_AO_B_RX
    8:      412,    # GPIOAO_0  | UART_AO_A_TXD
    10:     413,    # GPIOAO_1  | UART_AO_A_RXD
    12:     501,    # GPIOX_9   | SPI_A_MISO
    16:     502,    # GPIOX_10  | SPI_A_SS0     | I2C_EE_M1_SDA
    18:     500,    # GPIOX_8   | SPI_A_MOSI    | PWM_C
    22:     475,    # GPIOC_7
    24:     449,    # GPIOH_6   | UART_EE_C_RX  | SPI_B_SS0     | I2C_EE_M1_SDA
    28:     414,    # GPIOAO_2  | I2C_AO_M0_SCL | UART_AO_B_TX  | I2C_AO_S0_SCL
    32:     416,    # GPIOAO_4  | PWMAO_C
    36:     451,    # GPIOH_8
    38:     422,    # GPIOAO_10 | PWMAO_D
    40:     423,    # GPIOAO_11 | PWMAO_A
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
