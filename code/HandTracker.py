import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.modelComplexity=modelComplexity

        self.mpHands = mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,self.modelComplexity,self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils
    
    def findHands(self, img, draw=True):
        imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo=0, draw=True):
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        #print(id,cx,cy)
                        lmList.append((id,cx,cy))
                        #if id == 4:
                        if draw:
                            cv2.circle(img, (cx,cy), 15, (255,0,0), cv2.FILLED)
        return lmList
