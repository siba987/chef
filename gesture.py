from apds9960.const import *
from apds9960 import APDS9960
from picamera import PiCamera
from datetime import datetime
import RPi.GPIO as GPIO
import smbus
import time 
from time import sleep

port = 1
bus = smbus.SMBus(port)

apds = APDS9960(bus)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(38, GPIO.OUT)

camera = PiCamera()
cameraFlag = 0

#define callbacks
def intH(channel):
    print("take picture")

#def cameraFlash(channel):
#    print("make flash")
#    GPIO.output(38,GPIO.HIGH)

try:
    #interrupt event-driven
    GPIO.add_event_detect(7, GPIO.FALLING, callback = intH)
    apds.setProximityIntLowThreshold(50)
    
    print("Proximity Sensor test")
    print("========")
    apds.enableProximitySensor()
    oval=-1
    
    while True:
        sleep(0.25)
        val = apds.readProximity()
        if val != oval:
           print("proximity={}".format(val))
           if val > 60 and cameraFlag==0:
               print("val> 60, now to activate camera")
               GPIO.output(38,GPIO.HIGH)
               sleep(4)
               camera.capture('/home/pi/Desktop/webapp/static/latest.jpg')
               print("picture taken")
               cameraFlag =1

           elif val < 60:
               cameraFlag =0
               print("refrigerator is idling")
               GPIO.output(38,GPIO.LOW)
           oval =val
 
finally:
    GPIO.cleanup()
    camera.close()
    
print("Bye")
