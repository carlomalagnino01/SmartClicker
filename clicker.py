import cv2
import time
import HandTracker as ht
import pyautogui

wCam, hCam = 320,240

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3,wCam)
cap.set(4,hCam)

pTime=0
cTime=0
last=0
cur=0
detector=ht.handDetector(maxHands=1)

d=False
d1=False

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img, draw=False)

    if len(lmList)!=0:
        dist=((lmList[4][1]-lmList[8][1])**2+(lmList[4][2]-lmList[8][2])**2)**(1/2)
        dist1=((lmList[4][1]-lmList[12][1])**2+(lmList[4][2]-lmList[12][2])**2)**(1/2)

        if dist < 23:
            if not(d):
                pyautogui.press(['pagedown'])
            d=True
            cv2.circle(img, ((lmList[4][1]+lmList[8][1])//2,(lmList[4][2]+lmList[8][2])//2), 7, (255,0,0), cv2.FILLED)
        else:
            d=False
        if dist1 < 23:
            if not(d1):
                pyautogui.press(['pageup'])
            d1=True
            cv2.circle(img, ((lmList[4][1]+lmList[12][1])//2,(lmList[4][2]+lmList[12][2])//2), 7, (0,255,0), cv2.FILLED)
        else:
            d1=False

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime=cTime

    cv2.putText(img, f'FPS:{int(fps)}', (5,35), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)

    cv2.imshow("Smart_Clicker",img)
    cv2.setWindowProperty("Smart_Clicker", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(1)
    if cv2.getWindowProperty("Smart_Clicker", cv2.WND_PROP_VISIBLE) <1:
        break
cv2.destroyAllWindows()
