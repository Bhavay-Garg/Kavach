import cv2
import numpy as np
def preprocess(frame):
    lower = np.array([0, 0, 0])
    upper = np.array([179, 255, 120])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    erode = cv2.erode(mask, None, iterations=2)
    dilate = cv2.dilate(erode, None, iterations=2)
    cv2.imshow("Processed", frame) 
    cv2.waitKey(0)
    return dilate

img=cv2.imread("C:/Users/Bhavay Garg/Downloads/R2.jpg")
img_processed=preprocess(img)
cv2.imshow("Result",img_processed)
cv2.waitKey(0)
