# DJITello
Code to fly with a DJI Tello

![image](https://user-images.githubusercontent.com/74420584/191466513-9cdef492-a4a4-456b-ae8f-864b064c6054.png)




# DJI_tello_OpenCV_ColorObjectCenterRCCommands.py

dependencies :  

from djitellopy import Tello
import cv2, math, time
import numpy as np

![image](https://user-images.githubusercontent.com/74420584/191467167-d365271b-0329-44c2-98cb-5c19f1729c31.png)


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

# DJI_Tello_getBatteryStatus.py
Connect to your Tello drone to see it all works and get battery status indication.

# DJI_tello_set_wifi.py
An easy way to connect your DJI tello drone to your local Wifi Access point or Wifi router

# DJI_missionPad.py
This code will detect mission pads.
Use following code  detect a mission pad and measure distance.  The detection is based on an infrared sensor on the Tello
It does not use the camera, so the camera is free to use for other stuff
a guide can be found on :  https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20Mission%20Pad%20User%20Guide.pdf

# DJI_tello_swarm.py
Using DJI tello's in swarm configuration
You can only do this with DJI Tello EDU versions and you need to connect all drones to your local WIFI AP
based on SDK  https://djitellopy.readthedocs.io/en/latest/swarm/

# DJI_routeMissionPads.py
Fly from one missionpad to another
