# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 3
(https://linux-sunxi.org/images/5/50/OrangePi_3_Schematics_v1.5.pdf)

Usage:

.. code:: python
   import orangepi.3
   from OPi import GPIO

   GPIO.setmode(orangepi.3.BOARD) or GPIO.setmode(orangepi.3.BCM)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi 3 physical board pin to GPIO pin
BOARD = {
    3:  122,    # PD26/TWI0-SDA/TS3-D0/UART3-CTS/JTAG-DI
    5:  121,    # PD25/TWI0-SCK/TS3-DVLD/UART3-RTS/JTAG-DO
    7:  118,    # PD22/PWM0/TS3-CLK/UART2-CTS
    8:  354,    # PL2/S-UART-TX
    10: 355,    # PL3/S-UART-RX
    11: 120,    # PD24/TWI2-SDA/TS3-SYNC/UART3-RX/JTAG-CK
    12: 114,    # PD18/LCD0-CLK/TS2-ERR/DMIC-DATA3
    13: 119,    # PD23/TWI2-SCK/TS3-ERR/UART3-TX/JTAG-MS
    15: 362,    # PL10/S-OWC/S-PWM1
    16: 111,    # PD15/LCD0-D21/TS1-DVLD/DMIC-DATA0/CSI-D9
    18: 112,    # PD16/LCD0-D22/TS1-D0/DMIC-DATA1
    19: 229,    # PH5/SPI1-MOSI/SPDIF-MCLK/TWI1-SCK/SIM1-RST
    21: 230,    # PH6/SPI1-MISO/SPDIF-IN/TWI1-SDA/SIM1-DET
    22: 117,    # PD21/LCD0-VSYNC/TS2-D0/UART2-RTS
    23: 228,    # PH4/SPI1-CLK/PCM0-MCLK/H-PCM0-MCLK/SIM1-DATA
    24: 227,    # PH3/SPI1-CS/PCM0-DIN/H-PCM0-DIN/SIM1-CLK
    26: 360     # PL8/S-PWM0
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
