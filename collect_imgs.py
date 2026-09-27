import cv2

#open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print(f"FAIL: camera didnt open :(")

while(True):
    ret, frame = cap.read()
    frame =cv2.flip(frame, 1)
    if not ret: 
        print(f"Warning not captured")
    #display frame 
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
