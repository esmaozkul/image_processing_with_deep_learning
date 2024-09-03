# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:16:31 2024

@author: Esma
"""
import cv2
import numpy as np
#resimi içe aktar
img = cv2.imread("C:/Users/Esma/Desktop/python_proje/lenna.jpg")
cv2.imshow("orjinal",img)

#yatay
hor=np.hstack((img,img))
cv2.imshow("Horizontal", hor)

#dikey
ver=np.vstack((img,img))
cv2.imshow("dikey", ver)

#%%%
#perspektif ayarlama
import cv2
import numpy as np
img =cv2.imread("C:/Users/Esma/Desktop/python_proje/kart.png")
cv2.imshow("orjinal", img)

width=400
height=500

pts1=np.float32([[230,1],[1,472],[540,150],[338,617]])
pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

#nihadönüştürülmüş resim
imgOutput =cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("nihai resim",imgOutput)























