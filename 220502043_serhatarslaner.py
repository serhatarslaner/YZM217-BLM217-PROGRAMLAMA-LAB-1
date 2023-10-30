# Emir Dursun 220502001
# Serhat Arslaner 220502043

import ast
import time

print('''Asagidaki seceneklerin basindaki numaralari secerek istediginiz islemi yapabilirsiniz.

1-K'ninci en kucuk elemani bulma fonksiyonu
2-En yakin cifti bulma fonksiyonu
3-Bir listenin tekrar eden elemanlarini bulma fonksiyonu
4-Matris carpimi fonksiyonu
5-Bir text dosyasindaki kelimelerin frekansini bulma fonksiyonu
6-Liste icinde en kucuk degeri bulma fonksiyonu
7-Karekök fonksiyonu
8-EBOB bulma fonksiyonu
9-Asallik testi fonksiyonu
10-Hizli fibonacci hesabi fonksiyonu
11-Programi sonlandir.''')

#1
def k_kucuk(sira,liste):
    yeni_list=sorted(liste)
    sonuc=(yeni_list[int(sira)-1])
    
    return sonuc


#2
def en_yakin_cift(sayi,list1):  
    min_fark=1000000000

    for i in range(len(list1)):
        for j in range(i + 1,len(list1)):
            toplam=list1[i]+list1[j]
            fark=abs(sayi-toplam)

            if fark < min_fark:
                min_fark=fark
                en_yakin_cift = (list1[i]),"ve",(list1[j])
    return(en_yakin_cift)


#3
def tekrar_eden_elemanlar(liste):
    
    tekrar_edenler = list(set([x for x in liste if liste.count(x) > 1]))
    return tekrar_edenler


#4
def matris_carpimi(liste1,liste2):
    sonuc = []
    for satir in liste1:
        satir1 = []
        for sutun in zip(*liste2):
            toplam = 0
            for i in range(len(satir)):
                toplam = toplam + sutun[i]*satir[i]
            satir1.append(toplam)
        sonuc.append(satir1)
    return sonuc



#5
def kelime_frekans(dosya):

    with open(dosya,"r",encoding="utf-8") as text:
        kelime_list = text.read().strip().lower().split(" ")
    tek_list=[]
    for kelime in kelime_list:
        if tek_list.count(kelime)==1:
            continue
        else:
            tek_list.append(kelime)

    def sayac(kelime):
        return {kelime:kelime_list.count(kelime)}

    sonuc=list(map(sayac,tek_list))
    return sonuc

#6
def en_kucuk_deger(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        enKucuk = en_kucuk_deger(liste[1:])
        if liste[0] < enKucuk:
            return liste[0]
        else:
            return enKucuk


#7
def karekök(N, x_0, tol=10**(-10), maxiter=10, iterasyon=0):
    x_n = 0.5 * (x_0 + N / x_0)
    hata = abs(x_n**2 - N)
    if hata < tol:
        return x_n  
    if maxiter > iterasyon:
        return karekök(N, x_n, tol, maxiter, iterasyon+1)
    else:
        print("10 iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
        return x_n

#8
def eb_ortak_bolen(int1,int2):
        if int2 == 0:
            return int1
        else:
            return eb_ortak_bolen(int2, int1 % int2)

#9
def asal_veya_degil(n, i=2):
    
    if n == i:
        return True
    elif n % i == 0:
        return False
    return asal_veya_degil(n, i + 1)

#10
def fibonacci(n,k,fibk=1,fibk1=0):
    fib = [fibk1,fibk]
    print("n","k","fibk","fibk1")
    if k == 1:
        print(n,"1","1","0")
    while len(fib) < n:
        for i in range(2,n+1):
            fib.append(fib[-1] + fib[-2])
            if i >= k:
                print(n,i,fib[-1],fib[-2])

while True:
    
    secim=input("Seciminizi giriniz :")
    secim=secim.strip()
    secim = int(secim)

    if secim == 1:

        x=input("Listedeki en kucuk kacinci elemanin bulunacagini giriniz:")
        y=input("Istediginiz listeyi aralarinda virgul birakarak giriniz:")
        y=y.split(",")
        y = [int(sayi) for sayi in y]

        sonuc=k_kucuk(x,y)
        print(sonuc)
 
        
        
    elif secim == 2:

        x=int(input("Tam sayi degerini giriniz:"))
        y=input("Istediginiz listeyi sayilar arasinda virgul birakarak giriniz:")
        y=y.split(",")
        y = [int(sayi) for sayi in y]

        sonuc=en_yakin_cift(x,y)
        print(sonuc)
        

    
    elif secim == 3:
        x=input("Tekrar eden sayilari bulmak istediginiz listeyi virgul birakarak giriniz:")
        x=x.split(",")
        x = [int(sayi) for sayi in x]

        sonuc=tekrar_eden_elemanlar(x)
        print(sonuc)



    elif secim == 4:
        liste1=input("Istediginiz listeyi virgul birakarak giriniz: ")
        liste2=input("Carpim yapilacak olan ikinci listeyi virgul birakarak giriniz: ")
        liste1 = ast.literal_eval(liste1)
        liste2 = ast.literal_eval(liste2)
        print(matris_carpimi(liste1,liste2))



    elif secim == 5:
        x=input("Kelimeleri sayilacak olan dosya ismini girin: ")
        x = x + ".txt"
        print(kelime_frekans(x))



    elif secim == 6:
        x=input("En küçük elemanı bulmak istediginiz listeyi virgul birakarak giriniz:")
        x=x.split(",")
        x = [int(sayi) for sayi in x]
        print(en_kucuk_deger(x))  



    elif secim == 7:
        N = int(input("Verilen Sayı: "))
        x_0 = float(input("Tahmin Sayısı Giriniz: "))
        sonuc = karekök(N,x_0)
        print(sonuc)


    elif secim == 8:
        x=int(input("Ebobu bulunacak ilk sayiyi giriniz:"))
        y=int(input("Ebobu bulunacak ikinci sayiyi giriniz:"))
        sonuc=(eb_ortak_bolen(x,y))
        print(sonuc)

    elif secim == 9:
        x=input("Asal testi yapilacak sayiyi giriniz:")
        sonuc = (asal_veya_degil(int(x)))
        print(sonuc)

    
    elif secim == 10:
        n = int(input("n = hesaplanacak olan fibonacci sayısı: "))
        k = int(input("k = bugüne kadar gelinen yer ( başlatılacak yer): "))
        sonuc = (fibonacci(n,k))
        print(sonuc)


    elif secim == 11:
        print("Program Sonlandırılıyor...")
        time.sleep(3)
        break
    else:
        print("Yanlis secim,lutfen konsolda olan seceneklerden birini giriniz.")