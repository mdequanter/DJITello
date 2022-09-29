# This code will detect mission pads.
# Use following code  detect a mission pad and measure distance.  The detection is based on an infrared sensor on the Tello
# It does not use the camera, so the camera is free to use for other stuff
# a guide can be found on :  https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20Mission%20Pad%20User%20Guide.pdf# author : Maarten Dequanter
from djitellopy import Tello
import time


# If you have connected directly to your Tello Edu wifi network
#ipAddess = "192.168.10.1"
# If you have set your Tello Edu drone to connect to your AP
ipAddess = "192.168.0.82"

tello = Tello(ipAddess)
tello.connect()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)  # Both directions

minBattery = 20
battery = tello.get_battery()

print ("battery:"+str(battery)+"%")

if (battery < minBattery) :
    print ("Battery "+ str(battery) + "% => landing")


tello.takeoff()
pad = tello.get_mission_pad_id()


if (pad == 1) :
    print ("fly to pad 2")
    tello.go_xyz_speed(80,0,0,10)
    pad = tello.get_mission_pad_id()
    print ("found 2")
    if (pad == 2) :
        print ("found 2")
        distanceX = tello.get_mission_pad_distance_x()
        distanceY = tello.get_mission_pad_distance_y()
        distanceZ = tello.get_mission_pad_distance_z()
        tello.go_xyz_speed(-distanceX,-distanceY,0,10)
        print ("arrived at mission pad 2")
        tello.rotate_clockwise(90)
        tello.go_xyz_speed(90,0,0,10)
        print ("fly to mission pad 3")
        pad = tello.get_mission_pad_id()
        if (pad == 3) :
            print ("found 3")
            distanceX = tello.get_mission_pad_distance_x()
            distanceY = tello.get_mission_pad_distance_y()
            distanceZ = tello.get_mission_pad_distance_z()
            tello.go_xyz_speed(-distanceX,-distanceY,0,10)
            print ("arrived mission pad 3")

tello.land()

# graceful termination
tello.disable_mission_pads()
tello.land()
tello.end()