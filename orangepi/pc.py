"""
Alternative pin mappings for Orange PI PC(see
https://linux-sunxi.org/Xunlong_Orange_Pi_PC)

Usage:

.. code:: python
   import orangepi.pc
   from OPi import GPIO

   GPIO.setmode(orangepi.pc.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be 3 * 32 +14 = 110

BOARD = {
    3: 12,    # I2C0_SDA/PA12 (TWI0_SDA/DI_RX/PA_EINT12)
    5: 11,    # I2C0_SCL/PA11 (TWI0_SCK/DI_TX/PA_EINT11)
    7: 6,     # PA6 (SIM_PWREN/PWM1/PA_EINT6)
    8: 13,    # PA13 (SPI1_CS/UART3_TX/PA_EINT13)
    10: 14,   # PA14 (SPI1_CLK/UART3_RX/PA_EINT14)
    11: 1,    # PA1 (UART2_RX/JTAG_CK/PA_EINT1)
    12: 110,  # PD14
    13: 0,    # PA0 (UART2_TX/JTAG_MS/PA_EINT0)
    15: 3,    # PA3 (UART2_CTS/JTAG_DI/PA_EINT3)
    16: 68,   # PC4
    18: 71,   # PC7
    19: 64,   # PC0 (SPI0_MOSI)
    21: 65,   # PC1 (SPI0_MISO)
    22: 2,    # PA2 (UART2_RTS/JTAG_DO/PA_EINT2)
    23: 66,   # PC2 (SPI0_CLK)
    24: 67,   # PC3 (SPI0_CS)
    26: 21,   # PA21 (PCM0_DIN/SIM_VPPPP/PA_EINT21)
    27: 19,   # PA19 (PCM0_CLK/TWI1_SDA/PA_EINT19)
    28: 18,   # PA18 (PCM0_SYNC/TWI1_SCK/PA_EINT18)
    29: 7,    # PA7 (SIM_CLK/PA_EINT7)
    31: 8,    # PA8 (SIM_DATA/PA_EINT8)
    32: 200,  # PG8 (UART1_RTS/PG_EINT8)
    33: 9,    # PA9 (SIM_RST/PA_EINT9)
    35: 10,   # PA10 (SIM_DET/PA_EINT10)
    36: 201,  # PG9 (UART1_CTS/PG_EINT9)
    37: 20,   # PA20 (PCM0_DOUT/SIM_VPPEN/PA_EINT20)
    38: 198,  # PG6 (UART1_TX/PG_EINT6)
    40: 199,  # PG7 (UART1_RX/PG_EINT7)
}

# Orangepi PC BCM pin to actual GPIO pin
BCM = {
    2: 12,    # I2C0_SDA/PA12 (TWI0_SDA/DI_RX/PA_EINT12)
    3: 11,    # I2C0_SCL/PA11 (TWI0_SCK/DI_TX/PA_EINT11)
    4: 6,     # PA6 (SIM_PWREN/PWM1/PA_EINT6)
    14: 13,   # PA13 (SPI1_CS/UART3_TX/PA_EINT13)
    15: 14,   # PA14 (SPI1_CLK/UART3_RX/PA_EINT14)
    17: 1,    # PA1 (UART2_RX/JTAG_CK/PA_EINT1)
    18: 110,  # PD14
    27: 0,    # PA0 (UART2_TX/JTAG_MS/PA_EINT0)
    22: 3,    # PA3 (UART2_CTS/JTAG_DI/PA_EINT3)
    23: 68,   # PC4
    24: 71,   # PC7
    10: 64,   # PC0 (SPI0_MOSI)
    9: 65,    # PC1 (SPI0_MISO)
    25: 2,    # PA2 (UART2_RTS/JTAG_DO/PA_EINT2)
    11: 66,   # PC2 (SPI0_CLK)
    8: 67,    # PC3 (SPI0_CS)
    7: 21,    # PA21 (PCM0_DIN/SIM_VPPPP/PA_EINT21)
    0: 19,    # PA19 (PCM0_CLK/TWI1_SDA/PA_EINT19)
    1: 18,    # PA18 (PCM0_SYNC/TWI1_SCK/PA_EINT18)
    5: 7,     # PA7 (SIM_CLK/PA_EINT7)
    6: 8,     # PA8 (SIM_DATA/PA_EINT8)
    12: 200,  # PG8 (UART1_RTS/PG_EINT8)
    13: 9,    # PA9 (SIM_RST/PA_EINT9)
    19: 10,   # PA10 (SIM_DET/PA_EINT10)
    16: 201,  # PG9 (UART1_CTS/PG_EINT9)
    26: 20,   # PA20 (PCM0_DOUT/SIM_VPPEN/PA_EINT20)
    20: 198,  # PG6 (UART1_TX/PG_EINT6)
    21: 199,  # PG7 (UART1_RX/PG_EINT7)
}
