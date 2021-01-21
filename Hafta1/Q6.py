"""
Bir Pisagor üçlüsü, üç doğal sayı kümesidir.

a^{2}+b^{2}=c^{2}
Örneğin, 3^{2}+4^{2} = 9+16 = 5^{2}

Toplamı a + b + c = 1000 olan tam olarak bir Pisagor üçlüsü vardır.

abc çarpımını bulalım.
"""

for a in range(1, 1000): 
        for b in range(1,1000):
            c = 1000 - a - b  
            if a < b < c:
                if a**2 + b**2 == c**2:
                    print("A = ",a,"B = ",b,"C = ",c)
        
