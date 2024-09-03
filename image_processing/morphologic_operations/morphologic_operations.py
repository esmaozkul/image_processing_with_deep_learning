# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:22:12 2024

@author: Esma
"""

"""
5 çeşit morfolojik işlemler bulunmaktadır bunlar:
    -Erozyon:ön plandaki nesnenin sınırlarını asındırır
    -genişleme:görüntğüdeki beyaz bölgeyi artırır
    -açma:erozyon+genişletme (gürültününgiderilmesi için kullanılır)
    -kapatma: açmanın tam tersi genişleme +erozyon (küçük delikleriveya nesne uzerindeki küçük siyah noktaları kapatır)
    -morfolojik gradyan: bir görüntünün genişlemesi ve erozyonu arasındaki farktır
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np    
    
#resim içe aktar
img = cv2.imread("datai_team.jpg",0)       
plt.figure(),plt.imshow(img,cmap="gray"), plt.axis("off"),plt.title("orijinal img")

#erozyon
kernel=np.ones((5,5),dtype = np.uint8)
result =cv2.erode(img,kernel, iterations = 1)
plt.figure(),plt.imshow(result ,cmap="gray"), plt.axis("off"),plt.title("erozyon img")

#genişleme(dilation)
result2 =cv2.dilate(img,kernel, iterations = 1)
plt.figure(),plt.imshow(result2 ,cmap="gray"), plt.axis("off"),plt.title("dilation img")


#açılma için öncelikle beyaz gürültü ekleyelim resime fark edelim
whiteNoise=np.random.randint(0,2,size=img.shape[:2])
whiteNoise=whiteNoise*255
plt.figure(),plt.imshow(whiteNoise ,cmap="gray"), plt.axis("off"),plt.title("white Noise img")

noise_img =whiteNoise +img
plt.figure(),plt.imshow(noise_img ,cmap="gray"), plt.axis("off"),plt.title("noise img")

#açılma yöntemi (beyaz gürültüyü azaltmak için)
opening= cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN,kernel)
plt.figure(),plt.imshow(opening ,cmap="gray"), plt.axis("off"),plt.title("opening img")

#kapatmak  için öncelikle siyah gürültü ekleyelim resime fark edelim
blackNoise=np.random.randint(0,2,size=img.shape[:2])
blackNoise=whiteNoise*-255
plt.figure(),plt.imshow(blackNoise ,cmap="gray"), plt.axis("off"),plt.title("black Noise")

black_nois_img=blackNoise +img
black_nois_img[blackNoise<= -245]=0
plt.figure(),plt.imshow(black_nois_img ,cmap="gray"), plt.axis("off"),plt.title("black Noise img")

#kapatmak
closing= cv2.morphologyEx(black_nois_img.astype(np.float32), cv2.MORPH_CLOSE,kernel)
plt.figure(),plt.imshow(closing ,cmap="gray"), plt.axis("off"),plt.title("closing img")

#gradient= 
gradient= cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel)
plt.figure(),plt.imshow(gradient ,cmap="gray"), plt.axis("off"),plt.title("gradient img")



































