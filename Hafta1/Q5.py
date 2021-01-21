"""
    Üçüncü Veriseti A Sorusu

    Bu alıştırma için arkadaşlarımızın doğum günlerinin ne zaman olduğunu takip edeceğiz ve bu bilgileri isimlerine göre bulabileceğiz. 
    İsim ve doğum günlerinden oluşan bir sözlük (dosyası) oluşturalım. 
    Programımızı çalıştırdığınızda, kullanıcıdan bir isim girmesini ve o kişinin doğum gününü kendisine bildirmesini istemelidir. 
    Etkileşim şunun gibi görünmelidir:

"""

listemiz = {
    "Kemal Sunal":"10 Kasım 1944",
    "Adile Naşit":"17 Haziran 1930",
    "Münir Özkul":"15 Ağustos 1925",
    "Türkan Şoray":"28 Haziran 1945"
}

sorgu = input("Hangisinin doğum gününü öğrenmek istersin? Bu kişilerin doğum günlerini biliyoruz: \nKemal Sunal \nAdile Naşit \nMünir Özkul \nTürkan Şoray \n")

i = 0
for x in listemiz:
    if(x == sorgu):
        print(x,"'in doğum günü =", listemiz[x])
        i+=1
        break
if(i != 1):
    print("Bu kişi bulunmamaktadır !!")