# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 18:33:40 2024

@author: Esma
"""

#
"""
-Görüntünün düşük geçişli bir filtre uygulanmasıyla elde edilir.
-gürültüyü gidermek için kullanılır.(parazit kenarları kaldırır)
"""
# 
"""OpenCV , 3ana  tür bulanıklastırma bulmakta: ortalama ,gauss, medyan """
"""
Ortalama Bulanıklastırma : 
    bir görüntünün normalleştirilmiş bir kutu filitresiyle sarılmasıyla yapılır.
    Çekirdek alanın altındaki tüm piksellerin ort. alır ve bu ort. merkezi öge ile yer degiştirir.
Gauss Bulanıklastırma:
    kutu filtresi yerine gauss çekirdeği kullanır
    Pozitif ve tek olması gereken çekirdeğin genişlini ve yüksekliğini belirler.
    SigmaX ve sigmaY,X ve Y yönlerindeki standart sapmayı belirtmeliyiz.   
Medyan Bulanıklaştırma:
    Çekirdek alanı altındaki tüm piksellerin medyanını(ortadaki sayı) alır ve merkezi 
öge bu medyan değerle değiştirilir.
    Tuz ve biber gürültüsüne karşı oldukça etkilidir.  
"""

import cv2 
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# blurring ( detayı azaltır gürültüyü engeller)

img=cv2.imread("C:/Users/Esma/Desktop/python_proje/NYC.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

"""ortalama bulanıklastırma yöntemi"""
#dst2 rastgele bir değişken ismi değil opencv dökümanlarını cıktıları adlandırma sekli girdilerde src olarak adlandırışıyor
dst2=cv2.blur(img,ksize=(3,3))
plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("ort blur")
"""
gauss blur
"""
gb=cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("gauss blur")

"""
medyan blur
"""
mb=cv2.medianBlur(img, ksize=3)
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("medyan blur")


def gaussianNoise(image):
    row,col,ch=image.shape
    mean=0
    var=0.05
    sigma=var**0.5
    
    gauss=np.random.normal(mean,sigma,(row,col,ch))
    gauss=gauss.reshape(row,col,ch)
    noisy=image+gauss
    
    return noisy

#içe aktar ve normalize et.
img=cv2.imread("C:/Users/Esma/Desktop/python_proje/NYC.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

gaussianNoisyImage=gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("gauss Noisy"),plt.show()


#gauss blur uygulanırsa noisy azaltılır
gb2=cv2.GaussianBlur(gaussianNoisyImage, ksize=(3,3), sigmaX=7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("with gauss blur")

#tuz karabiber gürültüsü siyah beyaz noktaların rastgele olarak yerleştirilmesi durumu
def saltPepperNoise(image): 
    
    row,col,ch=image.shape 
    s_vs_p=0.5  #salt and pepper oranını yazıyoruz
    
    amount= 0.004
    
    noisy=np.copy(image)
    
    #salt : beyaz noktacık
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords=[np.random.randint(0,i-1,int(num_salt)) for  i in image.shape]
    noisy[coords] = 1
#peper :siyah noktacık
    num_pepper = np.ceil(amount * image.size * (1- s_vs_p))
    coords =[np.random.randint(0, i-1 ,int (num_pepper)) for  i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("sp Image")

mb2=cv2.medianBlur(spImage.astype(np.float32), ksize=3)
plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title("with medyan blur")

































