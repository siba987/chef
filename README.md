# Project Chef Jeff
![image](https://github.com/siba987/chef/assets/29061294/350e9015-142f-4068-8be1-cdff804f7cbc)

## Introduction to the Project
Our solution is an IoT device connected to an application which allows you to organize, diversify, and customize what you eat. The IoT device, which we call ‘Chef Jeff,’ has both eyes and ears, which allows you to view what’s in your fridge even while you are still at the office. He can also listen to you! Tell him commands such as “running low on milk” or “opened pasta sauce, expires in 7 days” and Chef Jeff will update Chef App. Chef App will then notify you the day before the pasta sauce will expire, to ensure you don’t waste it. 

This README.md file includes the code documentation for the Raspberry Pi Zero W with the following sensors:
* APDS9960 gesture sensor
* Microphone
* Speaker

### Software requirements
Python 3.7 (or 2.7+)
VNC Viewer or SSH tool to access Raspberry pi

### How to run

The two main scripts that were used are the following:
gesture.py - for the camera to take pictures when fridge is closed
speech.py - which integrates the Google Assistant SDK
upload.py - for sending the captured picture to Google drive
The first two files should be hosted locally on the Raspberry Pi zero w on independent Terminal windows. To edit the files on the Raspberry Pi, you can use any Text Editor tool (like GNU Nano, Vi, Vim, etc..)


### Raspberry Pi pinout
![ ](images/rasp-pi-zero-w.jpg)

### Other resources that were used in the project:

* https://github.com/liske/python-apds9960
* Google Assistant SDK - Google Developers
