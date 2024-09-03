# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:38:46 2024

@author: Esma
"""

#open cv ile nesne tespiti
#kenar algılama 
import cv2
import matplotlib.pyplot as plt
import numpy as np

img =cv2.imread("london.jpg",0)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off")

#kenarları çizmek için
edges=cv2.Canny(image=img, threshold1=0, threshold2=255)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.axis("off")

#medyan değeri140
med_val=np.median(img)
print(med_val)
#ortalama 12
# med_val=np.mean(img)
# print(med_val)
low=int(max(0,(1-0.33)*med_val))
high=int(min(255,(1+0.33)*med_val))

print(low)
print(high)
edges=cv2.Canny(image=img, threshold1=low, threshold2=high)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.axis("off")


#•blur
blurred_img=cv2.blur(img, ksize=(3,3))
plt.figure(),plt.imshow(blurred_img,cmap="gray"),plt.axis("off")

#blur değeri videodaki değere göre az da olsa farklı çıktı bunun nedeni ?ksize=(3,3) değerlerinden dolayı olabilir
med_val=np.median(blurred_img)
print(med_val)

low=int(max(0,(1-0.33)*med_val))
high=int(min(255,(1+0.33)*med_val))

print(low)
print(high)

edges=cv2.Canny(image=blurred_img, threshold1=low, threshold2=high)
plt.figure(),plt.imshow(edges,cmap="gray"),plt.axis("off")










