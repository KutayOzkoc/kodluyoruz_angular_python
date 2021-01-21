def kucuk(liste):
  a = min(liste)
  if(a == ""):
    return None
  else:
    return a

liste = [4,2,5]
print(kucuk(liste))