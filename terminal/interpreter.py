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
import numpy as np

class Interpreter():
	def __init__(self,terminal):
            self.terminal = terminal
            self.actions = {'shutdown': self.quit,
                            'q': self.quit,
                            'exit': self.quit,
                            'quit': self.quit,
                            'clear': self.clear,
                            'hello': self.convo,
                            'remember': self.memo,
                            'about': self.about,
                            'read': self.read,
                            'drive': self.drive}
		
	def cleanInput(self,inLine):
		inLine = inLine.rstrip()
		return inLine
		
	def Interpret(self,line):
		clean_line = self.cleanInput(line)
		words = clean_line.rsplit(' ')
                try:
                    f = self.actions[words[0]]
                except KeyError:
                    self.terminal.brain.phrase_queue("I'm sorry, I don't understand what you mean.",0)
                    return
                f(words)

        def quit(self, words):
            self.terminal.brain.say("Goodbye")
            self.terminal.log("Exiting Omni")
            self.terminal.brain.quit()

        def clear(self, words):
            if words[1] == 'logs':
                self.terminal.brain.say("Clearing Logs")
                self.terminal.clear_log()

        def convo(self, words):
            self.terminal.brain.say("What would you like to talk about?")

        def record(self, words):
	    if words[1] == 'audio':
                self.terminal.brain.say("Recording Audio")
	    elif words[1] == 'video':
                self.terminal.brain.say("Recording Video")

        def memo(self, words):
            self.terminal.brain.say("I'm sorry, right now my memory is really awful?")

        def read(self, words):
            if len(words) == 1:
                self.terminal.brain.prase_queue('I need to know what you want me to read.')
            elif len(words) > 1:
                if words[1] == 'news':   
                    if len(words) == 2:
                        src = 'AP/top_headlines'
                    else:
                        src = words[2]
                    news = self.terminal.brain.web.get_news(src)
                    for n in news:
                        sentc = n.split('.')
                        for s in sentc:
                            self.terminal.brain.phrase_queue(s,0)
                    self.terminal.brain.phrase_queue('That is all the news I found', 0)
                elif words[1] == 'joke':
                    joke = self.terminal.brain.web.get_joke()
                    sentc = joke.split('.')
                    for s in sentc:
                        self.terminal.brain.phrase_queue(s,0)
                
        def drive(self, words):
            d = words[1]
            if d == 'stop':
                self.terminal.brain.stop_moving()
            else:
                self.terminal.brain.drive(d)

        def about(self, words):
            if len(words) == 1:
                about_msg = self.terminal.brain.char.get_about_string(True)
                for msg in about_msg:
                    self.terminal.brain.voice.add_message(msg,0)
            elif words[1] == 'modules':
                modules = self.terminal.brain.modules
                self.terminal.brain.phrase_queue('I have ' + str(np.sum(modules.values())) + 'active modules, out of ' + str(len(modules)) + ' total modules',0)
                self.terminal.brain.phrase_queue('These include',0)
                for m in modules:
                    msg = m + ', which is '
                    if modules[m]:
                        msg += 'up'
                    else:
                        msg += 'down'
                    self.terminal.brain.phrase_queue(msg,0)

