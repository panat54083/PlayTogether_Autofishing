#ref = https://youtu.be/WymCpVUPWQ4
from cv2 import rectangle
import numpy as np
import pyautogui as pg
import cv2 as cv
import os
import time
from windowcapture import WindowCapture

window_name = "ApowerMirror Livestream"
# window_name = None
wincap = WindowCapture(window_name)

loop_time = time.time()
while(True):

    screenshot = wincap.get_screenshot()
    
    cv.imshow('Computer Vision', screenshot)

    print("FPS {}".format(1 / (time.time() - loop_time)))
    loop_time = time.time()
    key = cv.waitKey(1)
    # press "q" with the output windows focused to exist.
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)
        


print("Done...")