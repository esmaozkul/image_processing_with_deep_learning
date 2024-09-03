# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:33:52 2024

@author: Esma
"""
#%%
print("hello world")

#%% degiskenler(variable)

tamsayi_degisken=10
ondalikli_sayi=12.3

print(tamsayi_degisken)

# 4 islem ozellikleri

pi_sayisi=3.14
kat_sayi=2

toplam=pi_sayisi + 1
fark=pi_sayisi -1
carp=pi_sayisi * kat_sayi
bolme=pi_sayisi/kat_sayi

print("toplam:",toplam)
print("toplam {} ve fark {}".format(toplam,fark))
print("carpma: %.1f ,bolme: %.4f"%(carp,bolme))

#degiskenler arası donusum
carpma_int=int(carp)
print(carpma_int)

tamsayi_float  = float(tamsayi_degisken)
print(tamsayi_float)

#string:karakter dizileri

string="merhaba dunya"
print(string)

resim_yolu="veri"+"\\"+"img"+".png"
print(resim_yolu)

#%% python temel sozdizimi
#buyuk ve kucuk harf

temel =6

"""
bu kısımda sözdizimi çalışıyorum 
-buyuk harf
-kucuk harf
-yorum 
-girinti
-anahtar kelime 
"""
#girinti
if 5<10:
    print("yes")
else:
    print("no")    

#anahtar kelime 
de=4
#def=4

#sayili degisken
sayi=5
sayi2=2

#1sayi=7 seklinde yazilamaz

#%%
"""
-bileşik veri turudur ve cok yonludur
-[1,"a",1.0]
-farklı veri tiplerini içerisinde barındırabilir

"""
liste=[1,2,3,4,5,6]
print(type(liste))
hafta=["pazatesi","sali","carsamba","persembe","cuma","ctesi","pazar"]
#ilk eleman
print(hafta[0])

#son elaman 
print(hafta[6])

print(len(hafta))

print(hafta[len(hafta)-1])
print(hafta[-1])

#liste 2-3-4 : 1,2,3 indeks 
print(hafta[1:4]) #1 den 4 e kadar 1 dahil - 4 dahil degil

#sayi listesi

#eleman ekleme
sayi_listesi=[1,2,3,4,5,6]
sayi_listesi.append(7)
print(sayi_listesi)
#eleman silme
sayi_listesi.remove(4)
print(sayi_listesi)
#listeyi terse cevir
sayi_listesi.reverse()
print(sayi_listesi)
#listeyi sırala 
sayi_listesi=[1,2,3,4,5,67,0]
sayi_listesi.sort()
print(sayi_listesi)

# ½½ tuple 
"""
-değiştirelemez ve sıralı bir veri tipidir
(1,2,3)
"""

tuple_veritipi=(1,2,3,3,4,5,6)
#ilk eleman 
print (tuple_veritipi[0])

#2.indeksi
print (tuple_veritipi[2])

#count eleman 
print (tuple_veritipi.count(3))

tuple_xyz=(1,2,3)
x,y,z=tuple_xyz
print(x,y,z)

#%% deque

from collections import deque
dq=deque(maxlen=3)
dq.append(1)#1 ekle sonuna [1]
print(dq)

dq.append(2)#2 ekle sonuna [1,2]
print(dq)

dq.append(3)#3 ekle sonuna [1,2,3]
print(dq)

dq.append(4)#4 ekle sonuna [2,3,4]
print(dq)

dq=deque(maxlen=3)
dq.append(1)#1 ekle sonuna [1]
print(dq)
dq.append(2)# ekle sonuna [1,2]
print(dq)

dq.appendleft(3)#3 ekle sonuna [3,1,2]
print(dq)


#%%
"""
-bir çeşit karma tablo turudur 
-anahtar ve değer çiftlerinden oluşur
-{"anahtar": deger}
"""
dictionary={"istanbul":34,
            "izmir":35,
            "konya":42}
print(dictionary)

#istanbulun anahtar değeri
print(dictionary["istanbul"])

#anahtarlar
print(dictionary.keys())

#degerler
print(dictionary.values())

# history=["va_loss","val_acc","loss","acc"]

#%%kosullu ifadeler if else statment
"""
bir bool ifadesine göre doğru ya da yanlış olarak değerlendirilmesine 
bağlı olarak farklı hesaplar veya eylemeler gerçekleştiren
bir ifadedir.
"""
#buyuk kucuk sayı karsılastırması
sayi1=12.0
sayi2=20.0

if True: #true  yerine sayi1<sayi2 şeklinde de yazabiliriz.
    print("sayi 1 küçüktür sayi 2")
elif sayi1>sayi2:
    print("sayi 2 küçüktür sayi 1")
# elif sayi1==sayi2
else:
    print("sayi1 eşittir sayi2")

liste=[1,2,3,4,5]
deger=32

if deger in liste:
    print("{} deger listenin içerisindedir".format(deger))
else:
    print("{} deger listenin içerisinde değil".format(deger))

dictionary={"türkiye":"ankara","ingiltere":"londra","ispanya":"madrid"}

keys=dictionary.keys()
deger="türkiye"

if deger in keys:
    print("evet")
else: print("hayır")

bool1=True
bool2=False
if bool1 or bool2 :
    print("dogru")
else:print("yanlış")

if bool1 and bool2 :
    print("dogru")
else:print("yanlış")


#%%donguler
"""
bir dizi üzerinde yenileme yapmak için kullanılan yapılar 
-diziler: list,tuple,string,numpy pandas veri tipleri
"""
#for
for i in range (1,11):
    print(i)

liste=[1,4,5,6,8,3,3,4,67]
print(sum(liste))

for c in liste:
    print(c)

toplam=0
for c in liste:
    toplam=toplam+c
print(toplam)
"""
0=0+1
1=1+4
5=5+6
11=11+8
toplam=19...
"""
tup1=((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x,y,z)

# while dongusu
i=0
while i<4:
    print(i)
    i=i+1 #bu satırı eklemeseydik sonsuz döngü olurdu
    
liste=[1,4,5,6,8,3,3,4,67]
sinir=len(liste)

her=0
hesapla=0
while her< sinir:
      hesapla=hesapla+liste[her]    
      her= her+1
print(hesapla)

#%%fonksiyonlar
"""
-karmasık işlemleri toplar ve tek adımda yapmamızı sağlar
-şablon 
-düzenleme 
"""

#kullanıcı tarafından tanımlanan fonk.


def daireAlan(r):
    """
    Parameters
    ----------
    r : int - daire yarıçapı

    Returns
    -------
    daire_alani:float -daire alani

    """
    pi=3.14
    daire_alan = pi*(r**2)
    #print(daire_alan)
    return daire_alan

daireAlaniDegiskeni = daireAlan(3)

print(daireAlaniDegiskeni)

def daireCevre(r,pi=3.14):
   """
   Parameters
   ----------
   r : int - daire yarıçapı
   pi:float -pi sayısı
   Returns
   -------
   daire_cevre:float -daire cevresi
   """
    
   daire_cevre = 2*pi*r
    
   return daire_cevre

daireCevre=daireCevre(3,5) #pi 5 olur
print(daireCevre)

katsayi=5
def katsayiCarpimi():
    global katsayi
    print(katsayi*katsayi)
katsayiCarpimi()
print(katsayi)    

#bos fonk.
def bos():
    pass

#built in fonk.
liste=[1,2,3,4]
print(len(liste))
print(str(liste))
liste2=liste.copy()
print(liste2)
print(max(liste2))
print(min(liste))

#lamda fonk.
"""
ileri seviyeli
küçük ve ananim bir işlemdir

"""
def carpma(x,y,z):
    return x*y*z
sonuc=carpma(2,3,4)
print(sonuc)

#aynı islem with lambda
fonksiyon_lamda=lambda x,y,z : x*y*z
sonuc2=fonksiyon_lamda(2,3,4)
print(sonuc2)
#%%yield
"""
-iterasyon:yineleme
-generator
-yield
"""

liste=[1,2,3]
for i in liste:
    print(i)
    
""" 
generator yineleyicileri
generator degerleri bellekte saklanmaz yeri gelince anında üretirler
"""

generator =(x for x in range(1,4))    
for i in generator:
    print(i)

"""
fonksiyon eger return dondurecek ise bunu return yerine 
yield anahtar sözcugu ile yapar
"""
def creatGenerator ():
    liste=range(1,4)
    for i in liste:
        yield i
        
generator=creatGenerator()
print(generator)        

for i in generator:
    print(i)
"""bellekten yer kazanmak için kullanışlı bir yontem."""

#%%numpy kütüphanesi
"""
-matrisler için hesaplama kolaylıgı saglar
"""
import numpy as np
#1*15 boyutunda bir array-(dizi)

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape)#array'in boyutu

dizi2=dizi.reshape(3,5)

print("sekil:",dizi2.shape)
print("boyut:",dizi2.ndim)
print("veri tipi:",dizi2.dtype.name)
print("boy:",dizi2.size)

#array type
print("type:",type(dizi2))

# 2 boyutlu array
dizi2D=np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)

#sıfırlardan olusan bir array 
sifir_dizi=np.zeros((3,4))
print(sifir_dizi)

#birlerden olusan bir array 
bir_dizi=np.ones((3,4))
print(bir_dizi)

#bos array
bos_dizi=np.empty((3,4))
print(bos_dizi)

#arange(x,y,basamak)
dizi_aralik=np.arange(10,50,5)
print(dizi_aralik)

#linspace(x,y,basamak)
dizi_bosluk=np.linspace(10,20,5)
print(dizi_bosluk)


#matematiksel işlemler 
a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a-b)
print(a**b)

#dizi eleman toplama 
print(np.sum(a))

#max deger
print(np.max(a))

#min deger
print(np.min(a))

#mean ortalama 
print(np.mean(a))

#median ortalama 
print(np.median(a))

#rastgele sayı uretme [0,1]arasındaki sürekli uniform 3*3
rastgele_dizi=np.random.random((3,3))
print(rastgele_dizi)

#indeks
dizi=np.array([1,2,3,4,5,6,7])
print(dizi[0])

#dizinin ilk 4 elemanı 
print(dizi[0:4])

#dizinin tersi
print(dizi[::-1])

#
dizi2D=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1.satırı ve 1.sutununda bulunan elemanı
print(dizi2D[1,sayi1])

#1.sutun ve tum satırlar 
print(dizi2D[:,1])

#satır1,sutun 1,2,3
print(dizi2D[1,1:4])

#dizinin son satır tum sutunlar 
print(dizi2D[-1,:])

#
dizi2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

#vektor haline getirme
vektor=dizi2D.ravel()
print(vektor)

#
maksimum_sayinin_indeksi=vektor.argmax()
print(maksimum_sayinin_indeksi)

#%% pandas kütüphanesi
""" 
-hızlı güçlü ve esnek
"""
import pandas as pd

#sozluk olustur
dictionary={"isim":["ali","veli","kenan","murat","ayse","hilal"],
            "yas":[15,16,17,33,45,66],
            "maas":[100,150,240,350,110,220]}
veri= pd.DataFrame(dictionary)

#ilk 5 satır
print(veri.head())
print(veri.columns)

#veri bilgisi
print(veri.info())

#istatistiksel özellikler
print(veri.describe())
#yas sutunu
print(veri["yas"])
#sutun ekleme
veri["sehir"]=["ankara","istanbul","konya","izmir","bursa","antalya"]
print(veri)

#yas sutunu
print(veri.loc[:,"yas"])

#yas sutunu ve 3 satır
print(veri.loc[:3,"yas"])

#yas ve sehir arası sutunu ve 2 satır
print(veri.loc[:2,"yas":"sehir"])


#yas ve isim sutunu ve 2 satır
print(veri.loc[:2,["yas","isim"]])

#satırları tersten yazdır
print(veri.loc[::-1,:])

#yas sutunu with iloc
print(veri.iloc[:,1])

#ilk 3 satır ve yas ve isim
print(veri.iloc[:2,[0,1]])

#filitreleme

dictionary={"isim":["ali","veli","kenan","murat","ayse","hilal"],
            "yas":[15,16,17,33,45,66],
            "sehir":["izmir","ankara","konya","ankara","ankara","antalya"]}
veri= pd.DataFrame(dictionary)
print(veri)

#yasa göre filtre yas>22
filtre1=veri.yas>22
filitrelenmis_veri=veri[filtre1]
print(filitrelenmis_veri)

#ortalama yas
ortalama_yas=veri.yas.mean()

veri["yas_grubu"]=["kucuk" if ortalama_yas>i else "buyuk"for i in veri.yas]
print(veri)

#birlestirme
sozluk1={"isim":["ali","veli","kenan"],
            "yas":[15,16,17],
            "sehir":["izmir","ankara","konya"]}
veri1= pd.DataFrame(sozluk1)

sozluk2={"isim":["murat","ayse","hilal"],
            "yas":[33,45,66],
            "sehir":["ankara","ankara","antalya"]}
veri2= pd.DataFrame(sozluk2)

#dikey
veri_dikey=pd.concat([veri1,veri2],axis=0)

#yatay
veri_yatay=pd.concat([veri1,veri2],axis=1)

#%%matlotlib
"""
-görselleştirme
"""
import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4])
y=np.array([4,3,2,1])

plt.figure()
plt.plot(x,y,color="red",alpha=0.7,label="line")
plt.scatter(x, y, color="blue",alpha=0.4,label="scatter")
plt.title("Matlotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.xticks([0,1,2,3,4,5])
plt.legend()
plt.show()

fig, axes = plt.subplots(2,1,figsize=(9,7))
fig.subplots_adjust(hspace=0.5)

x=[1,2,3,4,5,6,7,8,9,10]
y=[10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(x,y)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")

#random resim
plt.figure()
img=np.random.random((50,50))
plt.imshow(img,cmap="gray")# 0(siyah) 1 (beyaz) 0.5 gri
# plt.axis("off")
plt.show()

#os kutuphanesi
import os
print(os.name)

currentDir=os.getcwd()
print(currentDir)

#new folder
folder_name="new_folder"
os.mkdir(folder_name)

new_folder_name="new_folder_2"
os.rename(folder_name,new_folder_name)

os.chdir(currentDir+"\\"+new_folder_name)
print(os.getcwd())

files=os.listdir()

for f in files:
    if f.endswith(".py"):
        print(f)
os.rmdir(new_folder_name)
for i in os.walk(currentDir):
    print(i)

os.path.exists("untitled0.py")



















