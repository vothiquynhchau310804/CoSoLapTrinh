def add(L,x,k):
    if k>len(L):
        L=L+[k]
    else:
        L=L[:k-1]+[x]+L[k-1:]
    return L
L=[1,2,3,4,5]
x=15
k=4
L=add(L,x,k)    
print(L)