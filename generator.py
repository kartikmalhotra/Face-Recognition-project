import cv2
import numpy as np
import pickle
import os

faceCascade =  cv2.CascadeClassifier('C:\\Users\\kartik\\Downloads\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
name=input("enter your name")
os.mkdir('K://prog//dataset//{}'.format(name))
k=1;
cap= cv2.VideoCapture(0)

while True:

    ret, image = cap.read()
    print(image)
    gray_image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5);  
    for (x, y, w, h) in faces:

            print(faces)
            cv2.imwrite('K://prog//dataset//{}//{}.jpg'.format(name,k),image)
            k +=1
            cv2.rectangle(image, (x-30, y-30), (x + w+30, y + h+30), (255, 255, 0), 2)
    
    cv2.imshow("image",image)
    
    k += 1
    if(k >60):
       break; 
    # if the 'q' key is pressed, stop the loop
        
    if (cv2.waitKey(1) == ord('q')):
        cap.release()
        break


cv2.destroyAllWindows()

