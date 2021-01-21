"""
İkinci Problem seti B sorusu

Diyelim ki bize bir değişkene kaydedilmiş bir liste vermiş olsunlar: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Bu listeyi alan ve içinde bu listenin yalnızca çift öğelerini içeren yeni bir liste oluşturan bir Python satırı yazın 
(ne kadar az satırda olursa o kadar iyidir :) ).
"""

a = [1,4,9,16,25,36,49,64,81,100]
ciftler =[]
i = 0

while i < len(a):
    if(a[i] % 2 == 0):
        ciftler.append(a[i])
    i+=1

"""

Test için Yazıldı

j = 0
while j < len(ciftler):
    print(ciftler[j])
    j+=1
"""