import cv2
import time

a=cv2.VideoCapture(0)
time.sleep(5)
check,frame=a.read()
cv2.imshow("Image",frame)
cv2.waitKey(0)
a.release()
cv2.destroyAllWindows()
