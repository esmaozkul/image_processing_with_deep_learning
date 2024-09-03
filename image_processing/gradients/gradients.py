# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:17:30 2024

@author: Esma
"""

#gradyanlar:görüntüdeki yoğunluk veya renkteki yönlü bir değişikliktir (kenar algılamada kullanılır)

import cv2
import  matplotlib.pyplot as plt

img=cv2.imread("sudoku.jpg",0)
plt.figure(),plt.imshow(img ,cmap="gray"), plt.axis("off"),plt.title("orijinal img")

#x gradyanı
sobelx=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0,ksize=5)
plt.figure(),plt.imshow(sobelx ,cmap="gray"), plt.axis("off"),plt.title("sobelx img")

#y gradyanı
sobely=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1,ksize=5)
plt.figure(),plt.imshow(sobely ,cmap="gray"), plt.axis("off"),plt.title("sobely img")

#♠laplaction gradyan
laplaction =cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure(),plt.imshow(laplaction ,cmap="gray"), plt.axis("off"),plt.title("laplaction img")














