# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:27:19 2024

@author: Esma
"""

#yaya algılama projesi
import cv2
import os

files =os.listdir()
#klasör olusturuyor 
img_path_list=[]

for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
         
print(img_path_list) 

#hog tanımlayıcısı=tesipit algoritması
hog=cv2.HOGDescriptor()

#tanımlacı svm ekle svm =Support vector machine (SVM) makine öğrenmesi algoritması genellikle sınıflandırma için kullanılır.
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#img döndürdürmek için döngü olusturduk
for imagePath in img_path_list:
    print(imagePath)
    
    image =cv2.imread(imagePath)
    
    (rects,weights)=hog.detectMultiScale(image,padding=(8,8),scale=1.05)
    for (x,y,w,h) in rects:
        cv2.rectangle(image, (x,y), (x+w,y+h),(0,0,255),2)
    
    
    cv2.imshow("yaya:",image)
    #yaya görsellerini klasorden sırayla q harfine tıkladıkça ilerlemesini sağlar
    if cv2.waitKey(0) & 0xFF == ord("q"): continue

        