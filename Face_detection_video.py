# This is the Python libary we are using to work with the face detector
import cv2
from random import randrange
import cvzone
import numpy as np

# the Classifier is the detector and cascade is the algorthm 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#  The imread will let the image be processed
#img = cv2.imread('friends.jpg')

#WE are going to use this fucnction to call video capture


video=cv2.VideoCapture("Basketball.mp4")
img2 = cv2.imread('Danny.PNG', cv2.IMREAD_UNCHANGED)

Gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


while True:
    #frame read is the boolean and fram is the acual image
    frame_read, frame = video.read()
    img2 = cv2.imread('Danny.PNG', cv2.IMREAD_UNCHANGED)
    Gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    scale = 1.0
    
    face_coordinates = trained_face_data.detectMultiScale(Gray_img)
    
    for (x,y,w,h) in face_coordinates:
        img2 = cv2.resize(img2, (w,h),None, scale,scale)
        frame = cvzone.overlayPNG(frame, img2, [x,y])
  
    cv2.imshow('dope ass', frame)
    cv2.waitKey(10)


