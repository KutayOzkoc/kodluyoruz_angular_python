def karekok(N,guess,hata):
    x_1 = 1
    ctr = 0
    a = []
    while x_1>=hata:
        x_1 = (guess + N/guess)/2
        ctr+=1
    a.append(x_1)
    a.append(ctr)
    return a

N = float(input("Karekök alınacak sayı : "))
guess = int(input("İlk tahmin : "))
hata = 10**(-10)

print(karekok(N,guess,hata))