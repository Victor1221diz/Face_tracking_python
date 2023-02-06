# This is the Python libary we are using to work with the face detector
import cv2
import re
from random import randrange
# the Classifier is the detector and cascade is the algorthm 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#  The imread will let the image be processed
pic = input("What image would you like Danny Devito in")
pattern = r".*\.(jpg|jpeg|png|gif)$"

if re.match(pattern, pic):
    cv2.imread(img = pic)
else:
    print('Error in picture, going into default')
    img = cv2.imread('friends.jpg')

# we  need to make the image graysale inorder for the algorhim to work
# and we do this with th cv2.cvtColor(image, The color)

Gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#the call to detect faces

face_coordinates = trained_face_data.detectMultiScale(Gray_img)

print(f'This is where the face is at{face_coordinates}')


for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y), (x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)

# this displace a retangle The to left are for the left bound and the right are for the right bounds
print(f'This is where the face is at{face_coordinates}')

#The imsshow will show is the image 
cv2.imshow('Face Detector',img)

#the wait key lets the image apper longer, other wise it will disapre instantly 

cv2.waitKey()


print('Code Completed')
#kasdlfkasjldfkjasd