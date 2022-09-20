# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# Based on the color you select, the Tello Edu will keep that object in the middle of your camera
# If possible use a mirror
# When starting the script the Tello will takeoff, pressing ESC makes it land
# and the script exit.
# based on SDK  https://djitellopy.readthedocs.io/en/latest/tello/



from djitellopy import Tello
import cv2, math, time
import numpy as np

tello_ip = '192.168.10.1'

tello = Tello(tello_ip)
tello.connect()



minBattery = 20

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


tello.takeoff()

distance = 20
minArea = 30


lower_Blue = np.array([100, 100, 50])
upper_Blue = np.array([130, 255, 255])
lower_Red = np.array([0, 143, 145])
upper_Red = np.array([179, 255, 255])


lower_color = lower_Red
upper_color = upper_Red

def findColor(img,lower_color,upper_color):
    radius = 0
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


while True:
    img = frame_read.frame
    battery = tello.get_battery()
    if (battery < minBattery) :
        print ("Battery "+ str(battery) + "% => landing")
        tello.land()
    text = "Battery: {}%".format(battery)
    cv2.putText(img, text, (5, 720 - 5),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    x,y,radius =  findColor(img,lower_color,upper_color)
    #print("x:"+ str(x) + " y:"+ str(y) + "radius:" + str(radius))
    cv2.circle(img, (int(x), int(y)), int(radius), (255, 0, 0), 5)
    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif (key == ord('z') or (x > (frameHeight/2 + 200)   and radius >= minArea)) :
        print("move forward")
        tello.move_forward(distance)
    elif (key == ord('s') or (x < (frameHeight/2 - 200)  and radius >= minArea)):
        print("move backward")
        tello.move_back(distance)
    elif (key == ord('a') or (y < (frameWidth/2 - 200)  and radius >= minArea)):
        tello.move_left(distance)
        print("move left")
    elif (key == ord('e') or (y > (frameWidth/2 - 200)  and radius >= minArea)):
        tello.move_right(distance)
        print("move right")
    elif key == ord('q'):
        print("rotate clockwize")
        tello.rotate_clockwise(distance)
    elif key == ord('d'):
        print("rotate counter clockwize")
        tello.rotate_counter_clockwise(distance)
    elif key == ord('u'):
        print ("move up")
        tello.move_up(30)
    elif key == ord('d'):
        print("move down")
        tello.move_down(30)
    elif key == ord('l'):
        print("Land")
        tello.land()
    elif key == ord('t'):
        print("Takeoff")
        tello.takeoff()
    cv2.imshow("drone", img)

tello.land()
