import math
def nhap():
    n=int(input('n='))
    return n
def lasonguyento(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def nextPrime(n):
    n=n+1
    while not lasonguyento(n):
        n += 1
    return n
def inkq(kq):
    print('So nguyen to lon hon n la:',kq)
n=nhap()
kq=nextPrime(n)
inkq(kq)


