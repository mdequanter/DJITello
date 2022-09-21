# DJITello
Code to fly with a DJI Tello




DJI_tello_OpenCV_ColorObjectCenterRCCommands.py

dependencies :  

from djitellopy import Tello
import cv2, math, time
import numpy as np


#  Demonstrating how to control a Tello using the stream of the onboard tello camera.
# Based on the color you select, the Tello Edu will keep that object in the middle of your camera
# If possible use a mirror
# When starting the script the Tello will takeoff, pressing Ctrl-c to end the script and make it land
# based on SDK  https://djitellopy.readthedocs.io/en/latest/tello/
# For help on OpenCV :  https://www.geeksforgeeks.org/python-programming-language/?ref=shm

# author Maarten Dequanter
# date 21/09/2022

Demonstration :  https://youtu.be/bJMtfXjVxwc

