#!/usr/bin/python2

import processing.brain
import sys

brain = processing.brain.Brain()

cycle = True
runtime = 0

while(cycle):
    brain.process()
    runtime += 1



