#!/usr/bin/python2

import RPi.GPIO as gpio
import time


class MotorController:

    def __init__(self):
        gpio.setmode(gpio.BOARD)

        self.pins = [7, 11, 13, 15]
        self.dirs = {'forward' : [True, False, True, False],
                     'backward': [False, True, False, True],
                     'left'    : [True, False, False, True],
                     'right'   : [False, True, True, False]}
        
        for pin in self.pins:
            gpio.setup(pin, gpio.OUT)

        self.stop()

    def drive(self, d):
        try:
            ctrl = self.dirs[d]
            for i in range(4):
                gpio.output(self.pins[i], ctrl[i])
        except KeyError:
            print "Unknown Direction"

    def stop(self):
        for p in self.pins:
            gpio.output(p, False)

    def cleanup(self):
        gpio.cleanup()

