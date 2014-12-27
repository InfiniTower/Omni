#!/usr/bin/python2

from pygsr import Pygsr
import pyaudio

class HearingModule:
    def __init__(self):
        self.speech = Pygsr()

    def listen(self, t):
        self.speech.record(t)
        phrase, complete_response  = self.speech.sepeech_to_text('en_EN')
        return phrase

    def connected(self):
        if self.speech:
            return True
        return False

    
