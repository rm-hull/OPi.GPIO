# -*- coding: utf-8 -*-
# Copyright (c) 2022 sillo01
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Zero2
(see https://linux-sunxi.org/File:Orange_Pi_Zero2_H616_Schematic_v1.3.pdf)
Usage:
.. code:: python
   import orangepi.zero2w
   from OPi import GPIO
   GPIO.setmode(orangepi.zero2w.BOARD)

 +------+-----+----------+--------+---+  ZERO2W  +---+--------+----------+-----+------+
 | GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
 +------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
 |      |     |     3.3V |        |   |  1 || 2  |   |        | 5V       |     |      |
 |  264 |   0 |    SDA.1 |    OFF | 0 |  3 || 4  |   |        | 5V       |     |      |
 |  263 |   1 |    SCL.1 |    OFF | 0 |  5 || 6  |   |        | GND      |     |      |
 |  269 |   2 |     PWM3 |    OFF | 0 |  7 || 8  | 0 | ALT2   | TXD.0    | 3   | 224  |
 |      |     |      GND |        |   |  9 || 10 | 0 | ALT2   | RXD.0    | 4   | 225  |
 |  226 |   5 |    TXD.5 |    OFF | 0 | 11 || 12 | 0 | OFF    | PI01     | 6   | 257  |
 |  227 |   7 |    RXD.5 |    OFF | 0 | 13 || 14 |   |        | GND      |     |      |
 |  261 |   8 |    TXD.2 |    OFF | 0 | 15 || 16 | 0 | OFF    | PWM4     | 9   | 270  |
 |      |     |     3.3V |        |   | 17 || 18 | 0 | OFF    | PH04     | 10  | 228  |
 |  231 |  11 |   MOSI.1 |    OFF | 0 | 19 || 20 |   |        | GND      |     |      |
 |  232 |  12 |   MISO.1 |    OFF | 0 | 21 || 22 | 0 | OFF    | RXD.2    | 13  | 262  |
 |  230 |  14 |   SCLK.1 |    OFF | 0 | 23 || 24 | 0 | OFF    | CE.0     | 15  | 229  |
 |      |     |      GND |        |   | 25 || 26 | 0 | ALT3   | CE.1     | 16  | 233  |
 |  266 |  17 |    SDA.2 |    OFF | 0 | 27 || 28 | 0 | OFF    | SCL.2    | 18  | 265  |
 |  256 |  19 |     PI00 |    OFF | 0 | 29 || 30 |   |        | GND      |     |      |
 |  271 |  20 |     PI15 |    OFF | 0 | 31 || 32 | 0 | OFF    | PWM1     | 21  | 267  |
 |  268 |  22 |     PI12 |    OFF | 0 | 33 || 34 |   |        | GND      |     |      |
 |  258 |  23 |     PI02 |    OFF | 0 | 35 || 36 | 1 | OUT    | PC12     | 24  | 76   |
 |  272 |  25 |     PI16 |    OFF | 0 | 37 || 38 | 0 | OFF    | PI04     | 26  | 260  |
 |      |     |      GND |        |   | 39 || 40 | 0 | OFF    | PI03     | 27  | 259  |
 +------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
 | GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
 +------+-----+----------+--------+---+  ZERO2W  +---+--------+----------+-----+------+
"""

# Orange Pi Zero 2w physical board pin to GPIO pin
# PH1(10) & PH2(11) for debug console default
BOARD = {
    3: 264,  # PI8 / TWI1_SDA
    5: 263,  # PI7 / TWI1_SCL
    7: 269,  # PI13 / PWM3 / UART4_TX
    8: 224,  # PH0 / UART0_TX
    10: 225,  # PH1 / UART0_RX
    11: 226,  # PH2 / UART5_TX
    12: 257,  # PI1
    13: 227,  # PH3 / UART5_RX
    15: 261,  # PI5 / TWI0_SCL / UART2_TX
    16: 270,  # PI14 / PWM4 / UART4_RX
    18: 228,  # PH4
    19: 231,  # PH7 / SPI1_MOSI
    21: 232,  # PH8 / SPI1_MISO
    22: 262,  # PI6 / TWI0_SDA / UART2_RX
    23: 230,  # PH6 / SPI1_CLK
    24: 229,  # PH5 / SPI1_CS0
    26: 233,  # PH9 / SPI1_CS1
    27: 266,  # PI10 / TWI2_SDA / UART3_RX
    28: 265,  # PI9 / TWI2_SCL / UART3_TX
    29: 256,  # PI0
    31: 271,  # PI15
    32: 265,  # PI11 / PWM1
    33: 268,  # PI12 / PWM2
    35: 258,  # PI2
    36: 76,  # PC12
    37: 272,  # PI16
    38: 260,  # PI4
    40: 259,  # PI3
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD
