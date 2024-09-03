# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:31:54 2024

@author: Esma
"""
import matplotlib.pyplot as plt
import os
# opencv kütüphanesini içe aktaralım
import cv2
# numpy kütüphanesini içe aktaralım
import numpy as np

# resmi siyah beyaz olarak içe aktaralım resmi çizdirelim
img= cv2.imread("C:/Users/Esma/Desktop/python_proje/odev2.jpg",0)
cv2.imshow("odev2", img)
# resim üzerinde bulunan kenarları tespit edelim ve görselleştirelim edge detection
edges = cv2.Canny(image=img, threshold1=200, threshold2=255)
cv2.imshow("kenar tespit", edges)
# yüz tespiti için gerekli haar cascade'i içe aktaralım
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# yüz tespiti yapıp sonuçları görselleştirelim
face_rect=face_cascade.detectMultiScale(img)
for(x,y,w,h) in face_rect:
    cv2.rectangle(img, (x,y),(x+w,y+h), (255,255,255),10)
cv2.imshow("yuz tespit",img)

# HOG ilklendirelim insan tespiti algoritmamızı çağıralım ve svm'i set edelim
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# resme insan tespiti algoritmamızı uygulayalım ve görselleştirelim
(rects,weigths)=hog.detectMultiScale(img,padding=(8,8),scale=1.05)

for(xA,yA,xB,yB) in rects:
    cv2.rectangle(img, (xA,yA),(xB,yB), (0,0,255),2)

cv2.imshow("insan tespiti",img)    