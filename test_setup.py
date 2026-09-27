import cv2
import mediapipe as mp
from sklearn.model_selection import train_test_split
import numpy as np

print(" all libraries have been imported correctly. :)")

#check that the hand attribute exists 
try: 
    mp.solutions.hands
    print("mp.solutions.hands is available! :)")

except AttributeError: 
    print("FAIL: mp.solutions must be missing in this mediapipe version :(")


# check the camera opens 

cap =cv2.VideoCapture(0)
if not cap.isOpened():
    print(f"FAIL: camera didnt open :(")
else:
    ret, frame = cap.read()
    if ret and frame is not None: 
        print(f"PASS: camera works! frame size {frame.shape} ")
    else: 
        print("FAIL: camera opened but could not read a frame :(")

#when everything is done, release the capture
cap.release()
