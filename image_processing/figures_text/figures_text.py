# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:00:20 2024

@author: Esma
"""

import cv2
import numpy as np 

#resim olustur
img=np.zeros((512,512,3),np.uint8) #siyah bir görüntü olusturuyorum
print(img.shape)

cv2.imshow("siyah", img)

#cizgi
#RGB red blue green(0,255,0) (BGR seklinde sıralıyor burası )
cv2.line(img,(0,0),(512,512),(0,255,0),3) #resim baslangıç noktası bitiş noktası renk kalınlık

cv2.imshow("cizgi", img)

#dikdörtgen 
#nesne tespiti sağlarken diktortgen içine almasında kullanacagız
cv2.rectangle(img, (0,0),(256,256),(255,0,0)) #cv2.FILLED  dersek içi dolu olur
cv2.imshow(("dikdortgen"), img)

#cember
#resim,merkez,yarıcap,renk ,
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED )
cv2.imshow("cember",img)

#metin
#resim baslangıc noktası font kalınlık renk
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("metin",img)




























