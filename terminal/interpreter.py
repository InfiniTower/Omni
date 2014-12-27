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

import sys

class Interpreter():
	def __init__(self,terminal):
		self.terminal = terminal
		
	# Strip input of '/n'
	def cleanInput(self,inLine):
		inLine = inLine.rstrip()
		return inLine
		
	def Interpret(self,line):
		clean_line = self.cleanInput(line)
		words = clean_line.rsplit(' ')
		
		if words[0] == 'shutdown' or words[0] == 'q':
                    self.terminal.brain.say("Goodbye")
                    self.terminal.log("Exiting Omni")
                    sys.exit(0)
		elif words[0] == 'clear':
			if words[1] == 'logs':
                            self.terminal.brain.say("Clearing Logs")
                            self.terminal.clear_log()
		elif words[0] == 'hello':
                            self.terminal.brain.say("What would you like to talk about?")
		elif words[0] == 'record':
			if words[1] == 'audio':
                            self.terminal.brain.say("Recording Audio")
			elif words[1] == 'video':
                            self.terminal.brain.say("Recording Video")
                elif words[0] == 'remember':
                    self.terminal.brain.say("What would you like me to remember?")

                elif words[0] == 'status':
                    status = self.terminal.brain.get_module_status()
                    for k in status:
                        expr = "Module " + k + "is "
                        if status[k]:
                            expr += " up."
                        else:
                            expr += " down."

                        self.terminal.brain.phrase_queue(expr,0)

		else:
			self.terminal.stdout(clean_line)
