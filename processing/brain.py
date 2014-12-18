import hearing.hearing
import vision.vision
import voice.speech
import personality.character

class Brain:
    def __init__(self):
        # Brain Components
        self.hear = hearing.hearing.HearingModule()
        self.vis = vision.vision.VisionModule()
        self.voice = voice.speech.SpeechModule()
        self.char = personality.character.Personality()

        self.voice.say("Hello, my name is " + self.char.get_property("name"))

    def process(self):
        self.vis.display()
