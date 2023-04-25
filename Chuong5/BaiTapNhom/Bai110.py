def SoHoanHao(n):
    tonguoc=0
    for i in range(1,n):
        if n%i==0:
            tonguoc+=i
    if tonguoc==n:
        return True
    else:
        return False
def Main():
    for i in range(1,10001):
        if SoHoanHao(i):
            print(i)
Main()