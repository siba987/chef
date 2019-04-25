from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from picamera import PiCamera
from datetime import datetime


gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)
camera = PiCamera()

filename = datetime.now().strftime("%H%M%S")+'.jpg'
print(filename)
camera.capture('/home/pi/Desktop/'+filename)

file1 = drive.CreateFile()
file1.SetContentFile(filename)
file1.Upload()
