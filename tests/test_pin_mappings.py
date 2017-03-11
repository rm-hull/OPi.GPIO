#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`OPi.pin_mappings` module.
"""

from OPi.pin_mappings import bcm, board, sunxi


def test_mappings():
    assert bcm(2) == board(3) == sunxi("PA12") == 12
    assert bcm(3) == board(5) == sunxi("PA11") == 11
    assert bcm(4) == board(7) == sunxi("PA06") == 6
    assert bcm(17) == board(11) == sunxi("PA01") == 1
    assert bcm(27) == board(13) == sunxi("PA00") == 0
    assert bcm(22) == board(15) == sunxi("PA03") == 3
    assert bcm(10) == board(19) == sunxi("PA15") == 15
    assert bcm(9) == board(21) == sunxi("PA16") == 16
    assert bcm(11) == board(23) == sunxi("PA14") == 14
    assert bcm(14) == board(8) == sunxi("PG06") == 198
    assert bcm(15) == board(10) == sunxi("PG07") == 199
    assert bcm(18) == board(12) == sunxi("PA07") == 7
    assert bcm(23) == board(16) == sunxi("PA19") == 19
    assert bcm(24) == board(18) == sunxi("PA18") == 18
    assert bcm(25) == board(22) == sunxi("PA02") == 2
    assert bcm(8) == board(24) == sunxi("PA13") == 13
    assert bcm(7) == board(26) == sunxi("PA10") == 10
