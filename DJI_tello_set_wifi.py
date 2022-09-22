# An easy way to connect your DJI tello drone to your local Wifi Access point or Wifi router
# After this procedure, the Tello will reboot and connect.  Use an IP scanner like advanced IP scanner or Angry IP on ubuntu to find the IP
# Or login to your router and look at the WIFI clients table
# To perform a factory reset, follow these steps
# Switch on the Tello drone and wait for the LEDs to flash yellow.
# Long press the power button for 5 seconds until the indicator light turns off. The indicator light starts to flash yellow. The Wi-Fi SSID and password will be reset to the factory settings and no password is set by default.



# author :  Maarten Dequanter

from djitellopy import Tello
import time


# First connect to your DJI tello with the standard setup
tello_ip = '192.168.10.1'

tello = Tello(tello_ip)
tello.connect()

ssid = "?????"
password = "???????"

tello.connect_to_wifi(ssid, password) 