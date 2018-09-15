Installation
------------
.. note:: The library has been tested against Python 2.7 and 3.4+.

   For **Python3** installation, substitute ``pip3`` for ``pip`` in the 
   instructions below.

Install the latest version of the library directly from
`PyPI <https://pypi.python.org/pypi?:action=display&name=OPi.GPIO>`_::

  $ sudo pip install --upgrade OPi.GPIO
  
Non Root Access
---------------
If you want to be able to use the library as a non root user, you will need to setup a `UDEV` rule to grant you permissions first. 
This can be accomplished as follows: 

``$ sudo usermod -aG gpio <current_user>``

``$ sudo nano /etc/udev/rules.d/99-gpio.rules``

That should add your user to the GPIO group, create a new ``UDEV`` rule, and open it in the Nano text editor. 

Enter the following into Nano


   SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'" 
   SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"



press ``ctrl-x``, ``Y``, and ``ENTER`` to save and close the file. 

Finally, reboot and you should be ready to use ``OPi.GPIO`` as a non root user. 
