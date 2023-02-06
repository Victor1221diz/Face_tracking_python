import cv2
import cvzone
import numpy as np



# the Classifier is the detector and cascade is the algorthm 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#  The imread will let the image be processed
img = cv2.imread('friends.jpg')
img2 = cv2.imread('Danny.PNG', cv2.IMREAD_UNCHANGED)

Gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


#the call to detect faces
face_coordinates = trained_face_data.detectMultiScale(Gray_img)
face_coordinates2 = trained_face_data.detectMultiScale(Gray_img2)
scale = 0.0

for (x,y,w,h) in face_coordinates:
    #cv2.rectangle(img, (x,y), (x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)


    
    img2 = cv2.resize(img2, dsize=(w,h))
    img = cvzone.overlayPNG(img, img2, [x,y])






cv2.imshow('Danny Devito in Friends', img)
cv2.waitKey(0)

print('Code Completed')
