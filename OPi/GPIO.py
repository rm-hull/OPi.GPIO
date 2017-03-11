# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull
# See LICENSE.md for details.

"""
Importing the module
--------------------
To import the RPi.GPIO module:

.. code:: python

   import OPi.GPIO as GPIO

By doing it this way, you can refer to it as just GPIO through the rest of your
script.

Pin Numbering
-------------
Pins on Orange Pi Zero are named PxNN where x = A..Z and NN = 00..99. This
implementation aims to paper over the cracks to make GPIO usage consistent
across Raspberry Pi and Orange Pi. Quoting from the RPi.GPIO documentation:

    *There are two ways of numbering the IO pins on a Raspberry Pi within
    RPi.GPIO. The first is using the BOARD numbering system. This refers to
    the pin numbers on the P1 header of the Raspberry Pi board. The advantage
    of using this numbering system is that your hardware will always work,
    regardless of the board revision of the RPi. You will not need to rewire
    your connector or change your code.*

    *The second numbering system is the BCM numbers. This is a lower level way
    of working - it refers to the channel numbers on the Broadcom SOC. You have
    to always work with a diagram of which channel number goes to which pin on
    the RPi board. Your script could break between revisions of Raspberry Pi
    boards.*

This library monkeys the original implementation (and the documentation, as you
are about to find out), by adding a third numbering system that is SUNXI naming.

Example Usage
-------------
1. First set up OPi.GPIO

    .. code:: python

       import OPi.GPIO as GPIO
       GPIO.setmode(GPIO.BOARD)
       GPIO.setup(12, GPIO.OUT)

2. To set an output high:

    .. code:: python

       GPIO.output(12, GPIO.HIGH)
       # or
       GPIO.output(12, 1)
       # or
       GPIO.output(12, True)

3. To set an output low:

    .. code:: python

       GPIO.output(12, GPIO.LOW)
       # or
       GPIO.output(12, 0)
       # or
       GPIO.output(12, False)

4. To output to several channels at the same time:

    .. code:: python

       chan_list = (11,12)
       GPIO.output(chan_list, GPIO.LOW) # all LOW
       GPIO.output(chan_list, (GPIO.HIGH,GPIO.LOW))  # first LOW, second HIGH

5. Clean up at the end of your program

    .. code:: python

       GPIO.cleanup()

Note that you can read the current state of a channel set up as an output using
the :py:meth:`input()` function. For example to toggle an output:

    .. code:: python

       GPIO.output(12, not GPIO.input(12))

Methods
-------
"""

from OPi.constants import HIGH, LOW, BCM, BOARD, SUNXI, IN, OUT  # noqa: F401
from OPi.pin_mappings import get_gpio_pin
from OPi import sysfs

_mode = None
_exports = []


def _check_configured(channel):
    if channel not in _exports:
        raise RuntimeError("Channel {0} is not configured".format(channel))


def getmode():
    """
    To detect which pin numbering system has been set

    :returns: GPIO.BOARD, GPIO.BCM, GPIO.SUNXI or None if not set.
    """
    return _mode


def setmode(value):
    """
    You must call this prior to using other calls. Typically, used as

    .. code:: python

       GPIO.setmode(GPIO.BCM)

    or

    .. code:: python

       GPIO.setmode(GPIO.BOARD)

    or

    .. code:: python

       GPIO.setmode(GPIO.SUNXI)

    """
    global _mode
    assert value in [BCM, BOARD, SUNXI]
    _mode = value


def setwarnings(enabled):
    pass


def setup(channel, direction, initial=None, pull_up_down=None):
    """
    You need to set up every channel you are using as an input or an output.
    To configure a channel as an input:

    .. code:: python

       GPIO.setup(channel, GPIO.IN)

    To set up a channel as an output:

    .. code:: python

       GPIO.setup(channel, GPIO.OUT)

    You can also specify an initial value for your output channel:

    .. code:: python

       GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

    **Setup more than one channel**
    You can set up more than one channel per call. For example:

    .. code:: python

       chan_list = [11,12]    # add as many channels as you want!
                              # you can tuples instead i.e.:
                              #   chan_list = (11,12)
       GPIO.setup(chan_list, GPIO.OUT)

    :param channel: the channel based on the numbering system you have
        specified (GPIO.BOARD, GPIO.BCM or GPIO.SUNXI).
    :param direction: whether to treat the GPIO pin as input or output
        (use only GPIO.IN or GPIO.OUT).
    :param initial: When supplied and setting up an output pin, resets
        the pin to the value given (can be 0 / GPIO.LOW / False or
        1 / GPIO.HIGH / True).
    """
    if isinstance(channel, list):
        for ch in channel:
            setup(ch, direction, initial, pull_up_down)
    else:
        if channel in _exports:
            raise RuntimeError("Channel {0} is already configured".format(channel))
        pin = get_gpio_pin(_mode, channel)
        sysfs.export(pin)
        sysfs.direction(pin, direction)
        if direction == OUT and initial is not None:
            sysfs.output(pin, initial)

        _exports.append(channel)


def input(channel):
    """
    To read the value of a GPIO pin:

    .. code:: python

       GPIO.input(channel)

    :param channel: the channel based on the numbering system you have
        specified (GPIO.BOARD, GPIO.BCM or GPIO.SUNXI).
    :returns: This will return either 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
    """
    _check_configured(channel)
    pin = get_gpio_pin(_mode, channel)
    return sysfs.input(pin)


def output(channel, state):
    """
    To set the output state of a GPIO pin:

    .. code:: python

       GPIO.output(channel, state)

    :param channel: the channel based on the numbering system you have
        specified (GPIO.BOARD, GPIO.BCM or GPIO.SUNXI).
    :param state: can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.

    **Output to several channels**
    You can output to many channels in the same call. For example:

    .. code:: python

       chan_list = [11,12]                             # also works with tuples
       GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
       GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW
    """
    if isinstance(channel, list):
        for ch in channel:
            output(ch, state)
    else:
        _check_configured(channel)
        pin = get_gpio_pin(_mode, channel)
        return sysfs.output(pin, state)


def cleanup(channel=None):
    """
    At the end any program, it is good practice to clean up any resources you
    might have used. This is no different with OPi.GPIO. By returning all
    channels you have used back to inputs with no pull up/down, you can avoid
    accidental damage to your Orange Pi by shorting out the pins. Note that
    this will only clean up GPIO channels that your script has used. Note that
    GPIO.cleanup() also clears the pin numbering system in use.

    To clean up at the end of your script:

    .. code:: python

       GPIO.cleanup()

    It is possible that don't want to clean up every channel leaving some set
    up when your program exits. You can clean up individual channels, a list or
    a tuple of channels:

    .. code:: python

       GPIO.cleanup(channel)
       GPIO.cleanup( (channel1, channel2) )
       GPIO.cleanup( [channel1, channel2] )
    """
    if channel is None:
        cleanup(_exports)
        _mode = None
    elif isinstance(channel, list):
        for ch in channel:
            cleanup(ch)
    else:
        _check_configured(channel)
        pin = get_gpio_pin(_mode, channel)
        sysfs.unexport(pin)
        _exports.remove(channel)
