from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
try:
    
    camera.capture('/home/pi/Desktop/webapp/templates/latest.jpg')
finally:
    camera.close()
