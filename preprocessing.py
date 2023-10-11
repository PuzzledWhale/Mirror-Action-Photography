import cv2
import time

def backgroundSubtract():

    cap = cv2.VideoCapture(0) # video capture (use 0 for default webcam for now)
    
    time.sleep(2) # pause for a bit to allow camera to open

    ret, background = cap.read() # the first frame read in is the background image

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # subtract frame from background image and apply a threshold to create a mask
        diff = cv2.absdiff(frame, background)
        diff_gray = diff.max(axis=2)
        _, fg_mask = cv2.threshold(diff_gray, 50, 255, cv2.THRESH_BINARY)

        result = cv2.bitwise_and(frame, frame, mask=fg_mask) # apply foreground mask to original frame

        cv2.imshow("Foreground Objects", result)

        if cv2.waitKey(30) & 0xFF == 27: # press 'esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
