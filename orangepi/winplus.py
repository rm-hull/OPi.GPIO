"""
Alternative pin mappings for Orange PI WinPlus(
https://linux-sunxi.org/images/6/6c/ORANGEPI-Winplus-V1_3.pdf
)

Usage:

.. code:: python
   import orangepi.winplus
   from OPi import GPIO

   GPIO.setmode(orangepi.winplus.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be 3 * 32 +14 = 110

BOARD = {
    3:  227,    # PH3/TWI1-SDA
    5:  226,    # PH2/TWI1-SCK
    7:  362,    # PL10/S-PWM
    8:  354,    # PL2/S-UART-TX
    10: 355,    # PL3/S-UART-RX
    11: 229,    # PH5/UART3-RX
    12: 100,    # PD4/LCD-D6/UART4-RTS/CCIR-D0
    13: 228,    # PH4/UART3-TX
    15: 231,    # PH7/UART3-CTS
    16: 361,    # PL9/S-TWI-SDA
    18:  68,    # PC4/NAND-CE0
    19:  98,    # PD2/LCD-D4/UART4-TX/SPI1-MOSI/CCIR-HSYNC
    21:  99,    # PD3/LCD-D5/UART4-RX/SPI1-MISO/CCIR-VSYNC
    22: 230,    # PH6/UART3-RTS
    23:  97,    # PD1/LCD-D3/UART3-RX/SPI1-CLK/CCIR-DE
    24:  96,    # PD0/LCD-D2/UART3-TX/SPI1-CS/CCIR-CLK
    26: 102,    # PD6/LCD-D10/CCIR-D2
    27: 143,    # PE15/TWI2-SDA
    28: 142,    # PE14/PLL-LOCK-DBG/TWI2-SCK
    29:  36,    # PB4/AIF2-SYNC/PCM0-SYNC
    31:  37,    # PB5/AIF2-BCLK/PCM0-BCLK
    32:  34,    # PB2/UART2-RTS/JTAG-DO0
    33:  38,    # PB6/AIF2-DOUT/PCM0-DOUT
    35:  39,    # PB7/AIF2-DINPCM0-DIN
    36:  35,    # PB3/UART2-CTS/I2S0-MCLK/JTAG-DI0
    37: 101,    # PD5/LCD-D7/UART4-CTS/CCIR-D1
    38:  32,    # PB0/UART2-TX/JTAG-MS0
    40:  33,    # PB1/UART2-RX/JTAG-CK0
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
