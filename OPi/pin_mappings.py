# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

import functools
from OPi.constants import BOARD, BCM, SUNXI, BOARD_DUO, BCM_DUO


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin
    BOARD: {
        3: 12,
        5: 11,
        7: 6,
        8: 198,
        10: 199,
        11: 1,
        12: 7,
        13: 0,
        15: 3,
        16: 19,
        18: 18,
        19: 15,
        21: 16,
        22: 2,
        23: 14,
        24: 13,
        26: 10
    },

    # BCM pin to actual GPIO pin
    BCM: {
        2: 12,
        3: 11,
        4: 6,
        7: 10,
        8: 13,
        9: 16,
        10: 15,
        11: 14,
        14: 198,
        15: 199,
        17: 1,
        18: 7,
        22: 3,
        23: 19,
        24: 18,
        25: 2,
        27: 0
    },
    
    # NanoPi Duo physical pin to actual GPIO pin
    BOARD_DUO: {
        3: 12,   # I2C0_SDA/GPIOA12
        5: 11,   # I2C0_SCL/GPIOA11
        7: 203,  # GPIOG11
        8: 198,  # UART1_TX/GPIOG6
        10: 199, # UART1_RX/GPIOG7 
        11: 5,   # DEBUG_RX(UART_RXD0)/GPIOA5/PWM0
        12: 363, # GPIOL11/IR-RX
        13: 4,   # DEBUG_TX(UART_TXD0)/GPIOA4 
        19: 15,  # UART3_RTS/SPI1_MOSI/GPIOA15
        21: 16,  # UART3_CTS/SPI1_MISO/GPIOA16
        23: 14,  # UART3_RX/SPI1_CLK/GPIOA14
        24: 13,  # UART3_TX/SPI1_CS/GPIOA13
        41: 355  # Button
    },

    # NanoPi Duo BCM pin to actual GPIO pin
    BCM_DUO: {
        2: 12,   # I2C0_SDA/GPIOA12
        3: 11,   # I2C0_SCL/GPIOA11
        4: 203,  # GPIOG11
        8: 13,   # UART3_TX/SPI1_CS/GPIOA13
        9: 16,   # UART3_CTS/SPI1_MISO/GPIOA16
        10: 15,  # UART3_RTS/SPI1_MOSI/GPIOA15
        11: 14,  # UART3_RX/SPI1_CLK/GPIOA14
        14: 198, # UART1_TX/GPIOG6
        15: 199, # UART1_RX/GPIOG7
        17: 5,   # DEBUG_RX(UART_RXD0)/GPIOA5/PWM0
        18: 363, # GPIOL11/IR-RX
        27: 4,   # DEBUG_TX(UART_TXD0)/GPIOA4
        41: 355  # Button
    },    

    SUNXI: _sunXi()
}


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
