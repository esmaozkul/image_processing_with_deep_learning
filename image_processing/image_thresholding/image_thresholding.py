# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:59:26 2024

@author: Esma
"""

#görüntü eşikleme 

import cv2 
import matplotlib.pyplot as plt

#resim içe aktar
img= cv2.imread("C:/Users/Esma/Desktop/python_proje/img1.JPG")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()

#esikleme
_, thresh_img=cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap="gray")
plt.axis("off")
plt.show()


#uyarlamalı esik degeri c sabiti 8 aldık  c sabitine göre ortalma deger alınıyor 
#11 de blok size piksel topluluğu 
thresh_img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh_img2,cmap="gray")
plt.axis("off")
plt.show()




















