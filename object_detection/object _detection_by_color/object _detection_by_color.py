# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:36:03 2024

@author: Esma
"""

import cv2
import numpy as np
from collections import deque

# Object center buffer size
buffer_size = 16
pts = deque(maxlen=buffer_size)

# Blue color range
blueLower = (84, 98, 0)
blueUpper = (179, 255, 255)

# Capture video
cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 480)

while True:
    success, imgOrjinal = cap.read()
    
    if success:
        
        # Blur
        blurred = cv2.GaussianBlur(imgOrjinal, (11, 11), 0)
        
        # HSV conversion
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv image", hsv)
        
        # Mask for blue color
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("mask image", mask)
        
        # Remove noise
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("mask+erozyon+genisleme", mask)
        
        # Find contours
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
        
        if len(contours) > 0:
            # Get the largest contour
            c = max(contours, key=cv2.contourArea)
            
            # Fit a rectangle
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x), np.round(y), np.round(width), np.round(height), np.round(rotation))
            print(s)
            
            # Get the box points
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            
            # Moments to find the center
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
            # Draw contour
            cv2.drawContours(imgOrjinal, [box], 0, (0, 255, 255), 2)
            
            # Draw the center point
            cv2.circle(imgOrjinal, center, 5, (255, 0, 255), -1)
            
            # Display information on screen
            cv2.putText(imgOrjinal, s, (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
            cv2.imshow("orjinal tespit", imgOrjinal)
            
            #deque
        pts.appendleft(center)   
        for i in range (1,len(pts)):
            if pts[i-1] is None or pts[i] is None : continue
        
            cv2.line(imgOrjinal, pts[i-1], pts[i], (0,255,0),3)
        
        cv2.imshow("orjinal tespit",imgOrjinal)    
        
        
        
        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
