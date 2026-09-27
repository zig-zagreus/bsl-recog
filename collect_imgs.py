import cv2
import os
import string


DATA_DIR = "data"
LETTERS = string.ascii_uppercase
TARGET_COUNT = 100

folder = os.path.join(DATA_DIR, LETTERS)


#open camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print(f"FAIL: camera didnt open :(")

# wrap in for loop to go over each letter of the alphabet 
for letter in LETTERS:
    folder = os.path.join(DATA_DIR, letter)
    os.makedirs(folder, exist_ok=True)
    
    #basic camera test
    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret: 
                        print(f"Warning not captured")
                        continue
        # display letter asked for 
        cv2.putText(frame, f"Letter: {letter}", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6)
        cv2.putText(frame, "Press SPACE when ready", (50, 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3) 
        #display frame 
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord(' '):
            break
        # save frame to folder/counter.jpg using cv2.imwrite
        
    counter = 0
    while(True):
        ret, frame = cap.read()
        if not ret: 
                print(f"Warning not captured")
                continue
        frame = cv2.flip(frame, 1)
        cv2.imshow('frame', frame)
        counter_str = str(counter)
        filename = os.path.join(folder, counter_str + ".jpg")
        cv2.imwrite(filename, frame)
        #increment 
        counter = counter + 1
        # once hit target break
        if counter == TARGET_COUNT: 
            break 
                

        if cv2.waitKey(20) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()

