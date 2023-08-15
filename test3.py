import requests
import torch

url = 'https://notify-api.line.me/api/notify'
token = 'ZdOhPxxgGLAHwmImh2I3J5A7gmDyzb8GKKi580W4Pnv'
headers = {
            'content-type':
            'application/x-www-form-urlencoded',
            'Authorization':'Bearer '+token
           }



name=['bkk']
# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path ='best.pt')

# Image

img =("datatest/01.jpg")
# Inference
results = model(img)
for detection in results.xyxy[0]:
    label = name[int(detection[5])]
    if label == 'bkk':
        r = requests.post(url, headers=headers , data = {'message':"HELLO BKK"})
    
