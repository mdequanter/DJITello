from djitellopy import Tello
import time

# If you have connected directly to your Tello Edu wifi network
#ipAddess = "192.168.10.1"
# If you have set your Tello Edu drone to connect to your AP
ipAddess = "192.168.0.86"


tello = Tello(ipAddess)
tello.connect()


battery = tello.get_battery()
print ("battery:"+str(battery)+"%")