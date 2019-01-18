OPi.GPIO
=========
.. image:: https://travis-ci.org/rm-hull/OPi.GPIO.svg?branch=master
   :target: https://travis-ci.org/rm-hull/OPi.GPIO

.. image:: https://coveralls.io/repos/github/rm-hull/OPi.GPIO/badge.svg?branch=master
   :target: https://coveralls.io/github/rm-hull/OPi.GPIO?branch=master

.. image:: https://img.shields.io/maintenance/yes/2018.svg?maxAge=2592000

.. image:: https://img.shields.io/pypi/pyversions/OPi.GPIO.svg
    :target: https://pypi.python.org/pypi/OPi.GPIO

.. image:: https://img.shields.io/pypi/v/OPi.GPIO.svg
   :target: https://pypi.python.org/pypi/OPi.GPIO

OPi-GPIO is a drop-in replacement library for `RPi.GPIO
<https://sourceforge.net/projects/raspberry-gpio-python/>`_ for the Orange Pi
Zero and other SBCs. Only the basic GPIO functions are replicated, using 
sysfs: this allows the GPIO pins to be accessed from user space.

.. toctree::
   :maxdepth: 3

   install
   api-documentation

.. include:: ../CONTRIBUTING.rst
.. include:: ../CHANGES.rst
.. include:: ../LICENSE.rst

