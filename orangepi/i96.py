"""
Alternative pin mappings for Orange PI PC(see
https://linux-sunxi.org/Xunlong_Orange_Pi_i96)
Usage:
.. code:: python
   import orangepi.i96
   from OPi import GPIO
   GPIO.setmode(orangepi.i96.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be 3 * 32 +14 = 110
BOARD = {
    3: 40,  # UART2.CTS
    5: 104,  # UART2.TX
    7: 103,  # UART2.RX
    8: 2,  # SPI2.CLK
    9: 41,  # UART2.RTS
    10: 4,  # SPI2.DI
    11: 14,  # UART1.CTS
    12: 6,  # SPI2.CS1
    13: 102,  # UART1.RX
    14: 3,  # SPI2.DO
    15: 0,  # I2C2.SCL
    16: 10,  # SPI2.CS0
    17: 1,  # I2C2.SDA
    18: 9,  # I2S.BCK
    19: 38,  # I2C3.SCL
    20: 13,  # I2S.DO
    21: 39,  # I2C3.SDA
    22: 11,  # I2S.DI
    23: 15,  # G.A A15
    24: 20,  # G.B A20
    25: 56,  # G.C B24
    26: 66,  # G.D D02
    27: 67,  # G.E D03
    28: 22,  # G.F A22
    29: 30,  # G.G A30
    30: 29,  # G.H A29
    31: 28,  # G.I A28
    32: 27,  # G.J A27
    33: 26,  # G.K A26
    34: 25,  # G.L A25
    101: 101,  # LED 1 next to USB A
    125: 125,  # LED 2 next to USB A
    126: 126,  # LED 3 next to USB A
}

# Orangepi PC BCM pin to actual GPIO pin
BCM = {  # SAME VALUES AS BOARD AS TEMPORARY FIX
    3: 40,  # UART2.CTS
    5: 104,  # UART2.TX
    7: 103,  # UART2.RX
    8: 2,  # SPI2.CLK
    9: 41,  # UART2.RTS
    10: 4,  # SPI2.DI
    11: 14,  # UART1.CTS
    12: 6,  # SPI2.CS1
    13: 102,  # UART1.RX
    14: 3,  # SPI2.DO
    15: 0,  # I2C2.SCL
    16: 10,  # SPI2.CS0
    17: 1,  # I2C2.SDA
    18: 9,  # I2S.BCK
    19: 38,  # I2C3.SCL
    20: 13,  # I2S.DO
    21: 39,  # I2C3.SDA
    22: 11,  # I2S.DI
    23: 15,  # G.A A15
    24: 20,  # G.B A20
    25: 56,  # G.C B24
    26: 66,  # G.D D02
    27: 67,  # G.E D03
    28: 22,  # G.F A22
    29: 30,  # G.G A30
    30: 29,  # G.H A29
    31: 28,  # G.I A28
    32: 27,  # G.J A27
    33: 26,  # G.K A26
    34: 25,  # G.L A25
    101: 101,  # LED 1 next to USB A
    125: 125,  # LED 2 next to USB A
    126: 126,  # LED 3 next to USB A
}
