# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.md for details.

import threading
import select

from select import EPOLLIN, EPOLLET, EPOLLPRI

from OPi.constants import NONE, RISING, FALLING, BOTH
from OPi import sysfs


_threads = {}


class _worker(threading.Thread):

    # TODO: implement bouncetime
    def __init__(self, pin, trigger, callback=None):
        super(_worker, self).__init__()
        self.daemon = True
        self._pin = pin
        self._trigger = trigger
        self._event_detected = False
        self._lock = threading.Lock()
        self._finished = False
        self._callbacks = []
        if callback is not None:
            self.add_callback(callback)

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def event_detected(self):
        with self._lock:
            if self._event_detected:
                self._event_detected = False
                return True
            else:
                return False

    def cancel(self):
        self._finished = True
        self.join()

    def run(self):
        self.exc = None
        try:
            sysfs.edge(self._pin, self._trigger)
            initial_edge = True

            with sysfs.value_descriptor(self._pin) as fd:
                e = select.epoll()
                e.register(fd, EPOLLIN | EPOLLET | EPOLLPRI)
                try:
                    while not self._finished:
                        events = e.poll(0.1, maxevents=1)
                        if initial_edge:
                            initial_edge = False
                        elif len(events) > 0:
                            with self._lock:
                                self._event_detected = True
                                self.notify_callbacks()

                finally:
                    e.unregister(fd)
                    e.close()

        except BaseException as e:
            self.exc = e

        finally:
            sysfs.edge(self._pin, NONE)

    def join(self):
        super(_worker, self).join()
        if self.exc:
            e = self.exc
            self.exc = None
            raise e

    def notify_callbacks(self):
        for cb in self._callbacks:
            cb(self._pin)


def blocking_wait_for_edge(pin, trigger, timeout=-1):
    assert trigger in [RISING, FALLING, BOTH]

    if pin in _threads:
        raise RuntimeError("Conflicting edge detection events already exist for this GPIO channel")

    try:
        sysfs.edge(pin, trigger)

        finished = False
        initial_edge = True

        with sysfs.value_descriptor(pin) as fd:
            e = select.epoll()
            e.register(fd, EPOLLIN | EPOLLET | EPOLLPRI)
            try:
                while not finished:
                    # TODO: implement bouncetime
                    events = e.poll(timeout / 1000.0, maxevents=1)
                    if initial_edge:
                        initial_edge = False
                    else:
                        finished = True

                n = len(events)
                if n == 0:
                    return None
                else:
                    return pin
            finally:
                e.unregister(fd)
                e.close()

    finally:
        sysfs.edge(pin, NONE)


def edge_detected(pin):
    if pin in _threads:
        return _threads[pin].event_detected()
    else:
        return False


def add_edge_detect(pin, trigger, callback=None):
    assert trigger in [RISING, FALLING, BOTH]

    if pin in _threads:
        raise RuntimeError("Conflicting edge detection already enabled for this GPIO channel")

    _threads[pin] = _worker(pin, trigger, callback)
    _threads[pin].start()


def remove_edge_detect(pin):
    if pin in _threads:
        _threads[pin].cancel()
        del _threads[pin]


def add_edge_callback(pin, callback):
    if pin in _threads:
        _threads[pin].add_callback(callback)
    else:
        raise RuntimeError("Add event detection before adding a callback")


def cleanup(pin=None):
    if pin is None:
        cleanup(list(_threads.keys()))
    elif isinstance(pin, list):
        for p in pin:
            cleanup(p)
    else:
        remove_edge_detect(pin)
