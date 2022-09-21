# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# Based on the color you select, the Tello Edu will keep that object in the middle of your camera
# If possible use a mirror
# When starting the script the Tello will takeoff, pressing ESC makes it land
# and the script exit.
# based on SDK  https://djitellopy.readthedocs.io/en/latest/tello/
# For help on OpenCV :  https://www.geeksforgeeks.org/python-programming-language/?ref=shm

# author Maarten Dequanter
# date 21/09/2022


onlyCamera = False   # set false if you want to fly, True if only camera

from djitellopy import Tello
import cv2, math, time
import numpy as np

tello_ip = '192.168.10.1'

tello = Tello(tello_ip)
tello.connect()



minBattery = 20
moveSpeed = 10

battery = tello.get_battery()

if (battery<minBattery) :
    print ("battery only: "+ str(battery) + "%, so cannot launch" )
    exit()


tello.streamon()
frame_read = tello.get_frame_read()
img = frame_read.frame



frameHeight = img.shape[0]
frameWidth = img.shape[1]
print('Frame Height       : ',frameHeight)
print('Frame Width        : ',frameWidth)


distance = 20
minArea = 20
marge = 80


lower_Blue = np.array([100, 100, 50])
upper_Blue = np.array([130, 255, 255])
lower_Red = np.array([0, 143, 145])
upper_Red = np.array([179, 255, 255])


lower_color = lower_Red
upper_color = upper_Red

def findColor(img,lower_color,upper_color):
    radius = 0
    x = 0
    y = 0
    img = cv2.GaussianBlur(img, (11, 11), 0)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    kernel = np.ones((9,9),np.uint8)
    mask = cv2.inRange(imgHSV, lower_color, upper_color)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    if len(cnts) > 0:
        # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        return x,y,radius
    else :
        return x,y,radius

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    if len(contours) > 0:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            print(area)
            if area>minArea:
                peri = cv2.arcLength(cnt,True)
                approx = cv2.approxPolyDP(cnt,0.02*peri,True)
                x, y, w, h = cv2.boundingRect(approx)
        return x+w//2, y    


def doMove(command):

    print (command)

    if (onlyCamera == False) :

        if (command == "F") :
            tello.send_rc_control(0, -moveSpeed, 0, 0)

        if (command == "B") :
            tello.send_rc_control(0, moveSpeed, 0, 0)

        if (command == "R") :
            tello.send_rc_control(moveSpeed, 0, 0, 0)

        if (command == "L") :
            tello.send_rc_control(-moveSpeed, 0, 0, 0)

        if (command == "LAND") :
            tello.land()
            exit()


        if (command == "TAKEOFF") :
            tello.takeoff()

        if (command == "MOVEUP") :
            tello.move_up(60)   


def setMarkers(img, battery):

    # Monitor battery level on top center of screen
    text = "Battery: {}%".format(battery)
    cv2.putText(img,text, (int(frameWidth/2)-80, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        

    # draw coordinates on screen to make it easy to navigate
    text = "x: 0, y:0"
    cv2.putText(img, text, (5, 20),
        cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
    text = "x: " + str(frameWidth) +", y:0"
    cv2.putText(img, text, (frameWidth-120, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    text = "x: 0, y:" + str(frameHeight)
    cv2.putText(img, text, (5, frameHeight-10),
        cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
    text = "x: " + str(frameWidth) +", y:" + str(frameHeight)
    cv2.putText(img, text, (frameWidth-120, frameHeight-10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # draw a box in center of 100x100px
    x1 = int((frameWidth/2)-50)
    y1 = int((frameHeight/2)-50)
    x2 = int((frameWidth/2)+50)
    y2 = int((frameHeight/2)+50)
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)

    return img



doMove("TAKEOFF")
doMove("MOVEUP")




while True:
    img = frame_read.frame
    img = cv2.flip(img,0)

    battery = tello.get_battery()
    if (battery < minBattery) :
        print ("Battery "+ str(battery) + "% => landing")
        doMove('LAND')
    img = setMarkers(img,battery)
    x,y,radius =  findColor(img,lower_color,upper_color)

    print("x:"+ str(x) + " y:"+ str(y) + "radius:" + str(radius))

    validObject = False
    if (radius >=minArea and x > 50 and x < frameWidth - 50  and y > 50 and y < frameHeight-50):
        validObject = True
        cv2.circle(img, (int(x), int(y)), int(radius), (255, 0, 0), 5)


    if (radius < minArea) :
        print ("No object found => Land")
        doMove('LAND')
    
    cv2.imshow("drone", img)
    cv2.waitKey(1)
    
    command = "K"
 
    if (y < (frameHeight/2 - marge)  and validObject == True) :
        command = "B"
    if (y > (frameHeight/2 + marge)  and validObject == True):
        command = "F"
    if (x < (frameWidth/2 - marge) and (y<(frameHeight/2 + marge) and y>(frameHeight/2 - marge))   and validObject == True):
        command = "L"
    if (x > (frameWidth/2 + marge) and (y<(frameHeight/2 + marge) and y>(frameHeight/2 - marge))  and validObject == True):
        command = "R"

    doMove(command)



    
    

doMove('LAND')
