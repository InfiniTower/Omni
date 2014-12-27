import cv2

class VisionModule:
    def __init__(self):
        self.dev = 0
        self.cap = cv2.VideoCapture(self.dev)

    def display(self):
        ret,frame = self.cap.read()
        if(ret):
            cv2.imshow('mirror',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass
    
    def connected(self):
        if self.cap:
            return True
        return False
