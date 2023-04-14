def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
            break
    return L
L=[1,2,3,4,5]
x=3
y=6
L=update(L,x,y)
print(L)        