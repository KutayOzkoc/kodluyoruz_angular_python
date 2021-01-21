import cmath 

def kokler(a,b,c):
    if a == 0 :
        print("sistemin tekli çözümü vardır")
        kok = -c / b 
        print(kok)
    else:
        delta = b * b - 4 * a * c

        if delta<0:
            print("sistemin reel kökü yoktur")
        elif delta == 0:
            kok = (-b - cmath.sqrt(delta)) / (2*a)
            print("sistemin tek bir reel kökü vardır")
            print(kok)
        else:
            print("sistemin iki farklı reel kökü vardır")
            kok1 = (-b - cmath.sqrt(delta)) / (2 * a)
            kok2 = (-b + cmath.sqrt(delta)) / (2 * a)
            print(kok1)
            print(kok2)

kokler(1,0,-4)
