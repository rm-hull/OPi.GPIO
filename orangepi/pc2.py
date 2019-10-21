"""
Alternative pin mappings for Orange PI PC 2(
https://linux-sunxi.org/images/c/cb/ORANGE_PI-PC2-V1_2_schematic.pdf
)

Usage:

.. code:: python
   import orangepi.pc2
   from OPi import GPIO

   GPIO.setmode(orangepi.pc2.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be 3 * 32 +14 = 110

BOARD = {
    3:   12,    # PA12/TWI0_SDA/DI_RX/PA_EINT12
    5:   11,    # PA11/TWI0_SCK/DI_TX/PA_EINT11
    7:    6,    # PA6/SIM_PWREN/PWM1/PA_EINT6
    8:   69,    # PC5/NAND_RE/SDC2_CLK
    10:  70,    # PC6/NAND_RB0/SDC2_CMD
    11:   1,    # PA1/UART2_RX/JTAG_CK0/PA_EINT1
    12: 110,    # PD14/RGMII_NULL/MII_TXERR/RMII_NULL
    13:   0,    # PA0/UART2_TX/JTAG_MS0/PA_EINT0
    15:   3,    # PA3/UART2_CTS/JTAG_DI0/PA_EINT3
    16:  68,    # PC4/NAND_CE0
    18:  71,    # PC7/NAND_RB1
    19:  15,    # PA15/SPI1_MOSI/UART3_RTS/PA_EINT15
    21:  16,    # PA16/SPI1_MISO/UART3_CTS/PA_EINT16
    22:   2,    # PA2/UART2_RTS/JTAG_DO0/PA_EINT2
    23:  14,    # PA14/SPI1_CLK/UART3_RX/PA_EINT14
    24:  13,    # PA13/SPI1_CS/UART3_TX/PA_EINT13
    26:  21,    # PA21/PCM0_DIN/SIM_VPPPP/PA_EINT21
    27:  19,    # PA19/PCM0_CLK/TWI1_SDA/PA_EINT19
    28:  18,    # PA18/PCM0_SYNC/TWI1_SCK/PA_EINT18
    29:   7,    # PA7/SIM_CLK/PA_EINT7
    31:   8,    # PA8/SIM_DATA/PA_EINT8
    32: 200,    # PG8/UART1_RTS/PG_EINT8
    33:   9,    # PA9/SIM_RST/PA_EINT9
    35:  10,    # PA10/SIM_DET/PA_EINT10
    36: 201,    # PG9/UART1_CTS/PG_EINT9
    37: 107,    # PD11/RGMII_NULL/MII_CRS/RMII_NULL
    38: 198,    # PG6/UART1_TX/PG_EINT6
    40: 199,    # PG7/UART1_RX/PG_EINT7
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
