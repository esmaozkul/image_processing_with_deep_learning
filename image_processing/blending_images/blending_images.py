# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:21:21 2024

@author: Esma
"""

#goruntuleri karısttırma

import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("C:/Users/Esma/Desktop/python_proje/img1.JPG")
img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2=cv2.imread("C:/Users/Esma/Desktop/python_proje/img2.JPG")
img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#aynı boyutta olmak zorunda oldugundan boyutları kontrol edelim
print(img1.shape)
print(img1.shape)

#bizde ikiside aynı boyutta cıktı eger aynı boyutta olmasaydı yazmamız gereken kod:
img1=cv2.resize(img1,(600,600))
print(img1.shape)

img2=cv2.resize(img2,(600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıstırılmıs resim =alpha*img1+beta*img2 seklinde hazır fonksiyonu => addWeighted
blended=cv2.addWeighted(src1=img1,alpha=0.5,src2=img2,beta=0.5,gamma=0)
plt.figure()
plt.imshow(blended)

































