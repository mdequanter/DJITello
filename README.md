# DJITello
Code to fly with a DJI Tello




# DJI_tello_OpenCV_ColorObjectCenterRCCommands.py

dependencies :  

from djitellopy import Tello
import cv2, math, time
import numpy as np


Demonstrating how to control a Tello using the stream of the onboard tello camera.
Based on the color you select, the Tello Edu will keep that object in the middle of your camera
If possible use a mirror
When starting the script the Tello will takeoff, pressing Ctrl-c to end the script and make it land
based on SDK  https://djitellopy.readthedocs.io/en/latest/tello/
For help on OpenCV :  https://www.geeksforgeeks.org/python-programming-language/?ref=shm

Demonstration :  https://youtu.be/bJMtfXjVxwc


# DJI_tello_detectColors.py

Selecting a color on a DJI Tello using the stream of the onboard tello camera.
select the right color using the HSV values.  Once you isolated your color
you can use the values that are printed in the terminal screen to set lower and upper values for your selected color
When starting the script you will see the tello stream, pressing Ctrl-c to end the script
based on SDK  https://djitellopy.readthedocs.io/en/latest/tello/
For help on OpenCV :  https://www.geeksforgeeks.org/python-programming-language/?ref=shm

![image](https://user-images.githubusercontent.com/74420584/191464840-a5dcf857-8ad6-4756-80a1-da60b2b0f7a6.png)



