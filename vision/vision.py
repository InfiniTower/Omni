import cv2

class VisionModule:
    def __init__(self):
        self.dev = 0
        self.cap = cv2.VideoCapture(self.dev)
        self.ret = 0
        self.frame = 0

    def blink(self):
        self.ret, self.frame = self.cap.read()

    def display(self):
        self.blink()
        if(self.ret):
            cv2.imshow('mirror',self.frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass
    
    def connected(self):
        self.blink()
        if self.ret:
            return True
        return False
