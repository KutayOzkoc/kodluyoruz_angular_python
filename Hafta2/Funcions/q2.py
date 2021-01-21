def recur_fibo(n):
    if n <= 2:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


nterms = 10
a = []
print("Fibonacci sequence:")
for i in range(nterms):
    a.append(recur_fibo(i))
a[0] = 1
print(a)
