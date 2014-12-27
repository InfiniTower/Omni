from subprocess import Popen

class SpeechModule:
    def __init__(self):
        self.path = "voice/googleSpeak.sh"
        self.var = "var/speaking.b"
        self.cur_priority = 0
        self.messages = {0: [],     # Conversation
                         1: [],     # Light Reminders
                         2: [],     # Important Reminders
                         3: [],     # 
                         4: []}     # System Critical Messages

    def say(self, text):
        Popen(["./" + self.path, '"' + text + '"'])

    def add_message(self, text, priority):
        self.messages[priority].append(text)
    
    def check_speaking(self):
        f = open(self.var)
        val = f.readline()
        val = val.rstrip()
        if val == "False":
            return False
        else:
            return True


    def update(self):
        if self.check_speaking():
            pass
        else:
            msg = ""
            for p in range(4,-1,-1):
                if len(self.messages[p]) > 0:
                    msg = self.messages[p].pop(0)
                    break
            if msg != "":
                self.say(msg)




