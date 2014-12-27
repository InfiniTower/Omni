#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 Patrick O'Neil <poneil@Faraday>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



"""Check for input every 0.1 seconds. Treat available input
immediately, but do something else if idle."""

import sys
import select
import time
import interpreter

logpath = 'data/logs/omni_terminal.log'

class TerminalInterface():
	def __init__(self,brain):
		self.timeout = 0.1 # seconds
		self.last_work_time = time.time()
		self.brain = brain
		self.print_arrow()
		self.interpreter = interpreter.Interpreter(self)
		
		self.logfile = open(logpath,'a')
		
		self.read_list = [sys.stdin]

	def print_arrow(self):
	  sys.stdout.write('> ')
	  sys.stdout.flush()
	  
	def clear_log(self):
		self.logfile.close()
		self.logfile = open(logpath,'w')
	  
	def get_brain(self):
		return self.brain
		
	def shutdown(self):
		self.logfile.close()
	  
	def update(self):
	  self.check_input()

	def treat_input(self,linein):
	  self.interpreter.Interpret(linein)
	  self.last_work_time = time.time()
	  self.print_arrow()

	def idle_work(self):
		pass

	def check_input(self):
		ready = select.select(self.read_list, [], [], self.timeout)[0]
		if not ready:
		  self.idle_work()
		else:
		  for file in ready:
			line = file.readline()
			if not line: # EOF, remove file from input list
			  self.read_list.remove(file)
			elif line.rstrip(): # optional: skipping empty lines
			  self.treat_input(line)
			  
	def stdout(self,out_string):
		logline = time.asctime() + ": " + out_string + "\n"
		self.logfile.write(logline)
		sys.stdout.write(out_string+"\n")
		sys.stdout.flush()

        def log(self, description):
		logline = time.asctime() + ": " + description + "\n"
		self.logfile.write(logline)
		
	def message(self,message):
		messArray = message.rsplit(" ")
		if messArray[0] == "print":
			self.stdout(messArray[1])
			self.print_arrow()

        def connected(self):
            if self.interpreter:
                return True
            return False



