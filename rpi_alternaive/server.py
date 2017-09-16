import io
import urllib
import cv2
import numpy as np
import time
from PIL import Image, ImageEnhance

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.225.229:8080/shot.jpg'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:

    content = urllib.urlopen(url).read()
    img = Image.open(io.BytesIO(content))
    contrast_enhancer = ImageEnhance.Contrast(img)
    pil_enhanced_image = contrast_enhancer.enhance(2)
    enhanced_image = np.asarray(pil_enhanced_image)
    r, g, b = cv2.split(enhanced_image)
    enhanced_image = cv2.merge([b, g, r])

    gray = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        img = cv2.rectangle(enhanced_image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = enhanced_image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            print "face found!"

    print "No face found!"