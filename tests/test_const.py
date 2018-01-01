#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`OPi.constants` module.
"""

import pytest
import OPi.constants as constants


def test_constants_cant_be_remapped():
    with pytest.raises(constants.ConstError) as ex:
        constants.HIGH = "banana"

    assert str(ex.value) == "Can't rebind const(HIGH)"
    assert constants.HIGH == 1
