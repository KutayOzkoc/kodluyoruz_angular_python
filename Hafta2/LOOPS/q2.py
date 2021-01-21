import math

def üstel(x, hata = 1e-10, maxterim = 50):
    n = 1
    a = list()
    ctr = 0
    sonterim = 1 # serideki ilk terimimiz
    toplam = sonterim
    while sonterim >= hata:
        if n > maxterim :
            print("{} terimde yakınsama sağlanamadı".format(maxterim))
            break
        sonterim = sonterim * x/n # yeni terim bir öncekini x ile çarpıp terim sıra numarasına bölerek bulunuyor.
        toplam += sonterim
        n += 1
        ctr+=1
        
    a.append(toplam)
    a.append(ctr)
    a.append(sonterim)
    return a


x = float(input("x degerini giriniz "))
sonuc = üstel(x)
print("e^x ~" , sonuc[0])
print(sonuc[1]," tane deger kullanıldı")
print(sonuc[2]," Son terimdir")



