from subprocess import Popen

class SpeechModule:
    def __init__(self):
        self.path = "voice/googleSpeak.sh"

    def say(self, text):
        Popen(["./" + self.path, '"' + text + '"'])
