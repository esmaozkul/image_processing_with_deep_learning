# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:27:09 2024

@author: Esma
"""

import cv2 

img=cv2.imread("C:/Users/Esma/Desktop/python_proje/ronaldo.jpg",0)

#gorsellestir
cv2.imshow("ilk resim", img)

k=cv2.waitKey(0) &0xFF

if k==27: #wsc
    cv2.destorAllWindows()
elif k== ord("s"):
    cv2.imwrite("C:/Users/Esma/Desktop/python_proje/ronaldo_gray.jpg", img)
    cv2.destroyAllWindows()

#%% video içe aktarma

import cv2
import time #videoyu yavaslatmamıza yaradı bu kodda 

#video ismini al
video_name="C:/Users/Esma/Desktop/python_proje/video.mp4"

#video içe aktar:capture,cap
cap=cv2.VideoCapture(video_name)
print("genislik:",cap.get(3))
print("yukseklik:",cap.get(4))

#videonun aktarılıp aktarılmadıgını anlamak için kontrol işlemi
while True:
    ret,frame=cap.read()
    if cap.isOpened()==False:
        print("hata")
    if ret == True:
       time.sleep(0.01) #uyarı* kullanmazsak çok hızlı akar
    
       cv2.imshow("video",frame)
    else : break
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cap.release() #stope capture
cv2.destroyAllWindows()    






















