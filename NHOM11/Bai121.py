def nhap():
    n=int(input("n="))
    L1=[]
    for i in range(n):
        L1+=[int(input())]
    max=int(input("max="))
    min=int(input("min="))
    return L1,max,min
def countrange(L1,max,min):
    L2=[]
    for i in range(len(L1)):
        if min<=L1[i]<max:
            L2+=[L1[i]]
    return L2
L1,max,min=nhap()
L2=countrange(L1,max,min)
print(len(L2))
print(L2)
        
    