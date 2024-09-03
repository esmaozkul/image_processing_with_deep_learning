# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:27:50 2024

@author: Esma
"""

#yeniden boyutlandırma ve kırpma

import cv2

img=cv2.imread("lenna.jpg")
print("resim boyutu:",img.shape)
cv2.imshow("orjinal",img)

#resized

imgRessized=cv2.resize(img,(800,800))
print("resized img shape:",imgRessized)
cv2.imshow("img resized",imgRessized)

#kırp
imgCropped = img[:100,:150] #benim resimim 255*255 oldugu için bu değerlerde denedim
cv2.imshow("kirpik resim", imgCropped)















