# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:33:02 2024

@author: Esma
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Kontur algılama
img = cv2.imread("contour.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")


contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

externel_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):
    # Externel
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(externel_contour, contours, i, 255, -1)
    else:  # Internal
        cv2.drawContours(internal_contour, contours, i, 255, -1)

plt.figure(), plt.imshow(externel_contour, cmap="gray"), plt.axis("off")
plt.figure(), plt.imshow(internal_contour, cmap="gray"), plt.axis("off")



   




















