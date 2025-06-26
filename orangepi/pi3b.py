# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 3B 1.1 (40-pin GPIO)
Product Page: http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-3B.html
PDF Doc File: https://drive.google.com/file/d/1i479ucxErqjL0GDakb5Bw85ptgnDf_Sc/view?usp=drive_link

Usage:

.. code:: python
   import orangepi.pi3b
   from OPi import GPIO

   # Choose pin numbering mode
   GPIO.setmode(orangepi.pi3b.BOARD) # Column Physical in table below
   GPIO.setmode(orangepi.pi3b.BCM) # Column GPIO in table below

   OPi.pin_mappings.set_custom_pin_mappings(orangepi.pi3b.WIRINGPI) # Set custom map of WiringPi
   GPIO.setmode(OPi.CUSTOM) # Column wPi in table below

+------+-----+----------+--------+---+   PI3B   +---+--------+----------+-----+------+
| GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
+------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
|      |     |     3.3V |        |   |  1 || 2  |   |        | 5V       |     |      |
|  140 |   0 |    SDA.2 |     IN | 1 |  3 || 4  |   |        | 5V       |     |      |
|  141 |   1 |    SCL.2 |     IN | 1 |  5 || 6  |   |        | GND      |     |      |
|  147 |   2 |    PWM15 |     IN | 0 |  7 || 8  | 1 | ALT1   | RXD.2    | 3   | 25   |
|      |     |      GND |        |   |  9 || 10 | 1 | ALT1   | TXD.2    | 4   | 24   |
|  118 |   5 | GPIO3_C6 |     IN | 0 | 11 || 12 | 1 | IN     | GPIO3_C7 | 6   | 119  |
|  128 |   7 | GPIO4_A0 |     IN | 0 | 13 || 14 |   |        | GND      |     |      |
|  130 |   8 |    TXD.7 |     IN | 0 | 15 || 16 | 0 | IN     | RXD.7    | 9   | 131  |
|      |     |     3.3V |        |   | 17 || 18 | 0 | IN     | GPIO4_A1 | 10  | 129  |
|  138 |  11 | SPI3_TXD |     IN | 0 | 19 || 20 |   |        | GND      |     |      |
|  136 |  12 | SPI3_RXD |     IN | 0 | 21 || 22 | 0 | IN     | TXD.9    | 13  | 132  |
|  139 |  14 | SPI3_CLK |     IN | 0 | 23 || 24 | 0 | IN     | SPI3_CS1 | 15  | 134  |
|      |     |      GND |        |   | 25 || 26 | 0 | IN     | GPIO4_A7 | 16  | 135  |
|   32 |  17 |    SDA.3 |   ALT2 | 1 | 27 || 28 | 1 | ALT2   | SCL.3    | 18  | 33   |
|  133 |  19 |    RXD.9 |     IN | 0 | 29 || 30 |   |        | GND      |     |      |
|  124 |  20 | GPIO3_D4 |     IN | 0 | 31 || 32 | 0 | IN     | PWM11    | 21  | 144  |
|  127 |  22 | GPIO3_D7 |     IN | 0 | 33 || 34 |   |        | GND      |     |      |
|  120 |  23 | GPIO3_D0 |     IN | 0 | 35 || 36 | 0 | IN     | GPIO3_D5 | 24  | 125  |
|  123 |  25 | GPIO3_D3 |     IN | 0 | 37 || 38 | 0 | IN     | GPIO3_D2 | 26  | 122  |
|      |     |      GND |        |   | 39 || 40 | 0 | IN     | GPIO3_D1 | 27  | 121  |
+------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
| GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
+------+-----+----------+--------+---+   PI3B   +---+--------+----------+-----+------+

"""



# Orange Pi 3b physical board pin to GPIO pin
BOARD = {
    3:  140,    # SDA.2/GPIO4_B4
    5:  141,    # SCL.2/GPIO4_B5
    7:  147,    # PWM15/GPIO4_A4
    8:  25,     # RXD.2/GPIO0_D1
    10: 24,     # TXD.2/GPIO0_D0
    11: 118,    # GPIO3_C6
    12: 119,    # GPIO3_C7
    13: 128,    # GPIO4_A0
    15: 130,    # TXD.7/GPIO4_A2
    16: 131,    # RXD.7/GPIO4_A3
    18: 129,    # GPIO4_A1
    19: 138,    # SPI3_TXD/GPIO4_B2
    21: 136,    # SPI3_RXD/GPIO4_B0
    22: 132,    # TXD.9/GPIO4_B1
    23: 139,    # SPI3_CLK/GPIO4_B3
    24: 134,    # SPI3_CS1/GPIO4_A6
    26: 135,    # GPIO4_A7
    27: 32,     # SDA.3/GPIO4_A0
    28: 33,     # SCL.3/GPIO1_A1
    29: 133,    # RXD.9/GPIO4_A5
    31: 124,    # GPIO3_D4
    32: 144,    # PWM11/GPIO4_C0
    33: 127,    # GPIO3_D7
    35: 120,    # GPIO3_D0
    36: 125,    # GPIO3_D5
    37: 123,    # GPIO3_D3
    38: 122,    # GPIO3_D2
    40: 121,    # GPIO3_D1
}

# Orange Pi 3b physical board pin to WiringPi GPIO pin
WIRINGPI = {
    3:  0,   # SDA.2/GPIO4_B4
    5:  1,   # SCL.2/GPIO4_B5
    7:  2,   # PWM15/GPIO4_A4
    8:  3,   # RXD.2/GPIO0_D1
    10: 4,   # TXD.2/GPIO0_D0
    11: 5,   # GPIO3_C6
    12: 6,   # GPIO3_C7
    13: 7,   # GPIO4_A0
    15: 8,   # TXD.7/GPIO4_A2
    16: 9,   # RXD.7/GPIO4_A3
    18: 10,  # GPIO4_A1
    19: 11,  # SPI3_TXD/GPIO4_B2
    21: 12,  # SPI3_RXD/GPIO4_B0
    22: 13,  # TXD.9/GPIO4_B1
    23: 14,  # SPI3_CLK/GPIO4_B3
    24: 15,  # SPI3_CS1/GPIO4_A6
    26: 16,  # GPIO4_A7
    27: 17,  # SDA.3/GPIO4_A0
    28: 18,  # SCL.3/GPIO1_A1
    29: 19,  # RXD.9/GPIO4_A5
    31: 20,  # GPIO3_D4
    32: 21,  # PWM11/GPIO4_C0
    33: 22,  # GPIO3_D7
    35: 23,  # GPIO3_D0
    36: 24,  # GPIO3_D5
    37: 25,  # GPIO3_D3
    38: 26,  # GPIO3_D2
    40: 27,  # GPIO3_D1
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
