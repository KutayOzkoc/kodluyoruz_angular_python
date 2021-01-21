def main(n):
    liste = [1,2]
    for i in range(3,n):
        count = 0
        while i > len(liste):
            if i % 2 == 0:
                i = i/2
            else:
                i = 3*i+1
            count += 1
        liste.append(count + liste[int(i)-1])
    return liste.index(max(liste))+1

print(main(1000000))