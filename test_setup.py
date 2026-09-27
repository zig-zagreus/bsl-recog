import cv2
import mediapipe as mp
from sklearn.model_selection import train_test_split


print(" all libraries have been imported correctly. :)")

#check that the attribute exists 
try: 
    mp.solutions.hands
    print("mp.solutions.hands is available! :)")

except AttributeError: 
    print("FAIL: mp.solutions must be missing in this mediapipe version :(")
