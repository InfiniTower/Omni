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

        self.update_module_status()
        self.modules = {"audio" : False,
                        "vision" : False,
                        "voice" : False,
                        "term" : False}


        self.voice.add_message("Hello",0)

    def process(self):
        self.update_module_status()
        if self.modules["vision"]:
            self.vis.display()

        if self.modules["voice"]:
            self.voice.update()

        if self.modules["term"]:
            self.term.update()

    def say(self, text):
        if self.modules['voice']:
            self.voice.say(text)

    def phrase_queue(self, text, pri):
        if self.modules['voice']:
            self.voice.add_message(text, pri)

    def update_module_status(self):
        self.modules = {"audio" : False,
                        "vision" : False,
                        "voice" : False,
                        "term" : False}

        if self.hear.connected():
            self.modules["audio"] = True

        if self.vis.connected():
            self.modules["vision"] = True
        
        if self.voice.connected():
            self.modules["voice"] = True
        
        if self.term.connected():
            self.modules["term"] = True

    def get_module_status(self):
        self.update_module_status()
        return self.modules

        
