def mukemmel(sayi):
    çarpanlar=[]
    x=1
    while x < sayi :
        if sayi % x == 0 :
            çarpanlar.append(x)
        x+=1
    
    toplam = sum(çarpanlar)
    if toplam == sayi :
        return True 
    else:
        return False

print(mukemmel(10))