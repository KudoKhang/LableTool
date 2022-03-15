import cv2
import numpy as np

human_mask = cv2.imread('RawData/matting_4.png')
clothes_mask = cv2.imread('RawData/Image_4.png')

skin = human_mask - clothes_mask
skin_gray = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)

contours, hierarchy = cv2.findContours(skin_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 4000:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        cv2.rectangle(skin_gray, (x, y), (x + w, y + h), (255, 255, 0), 2)
        print(area, (x, y, w, h))
        points = np.array([(x, y), (x + w, y), (x + w, y + h), (x, y + h)])
        # cv2.fillPoly(skin_gray, pts = [points], color = (0, 0, 0))
cv2.imshow('skin', skin_gray)
cv2.waitKey(0)