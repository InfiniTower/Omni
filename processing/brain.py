import hearing.hearing
import vision.vision
import voice.speech
import personality.character
import timer.timer
import terminal.terminal

class Brain:
    def __init__(self):
        # Brain Components
        self.hear = hearing.hearing.HearingModule()
        self.vis = vision.vision.VisionModule()
        self.voice = voice.speech.SpeechModule()
        self.char = personality.character.Personality()
        self.time = timer.timer.TimeModule()
        self.term = terminal.terminal.TerminalInterface(self)
        self.term.log("Beginning Omni")

        self.voice.add_message("Hello",0)

    def process(self):
        self.vis.display()
        self.voice.update()
        self.term.update()

    def say(self, text):
        self.voice.say(text)
        
