L=[1,2,3,4,5,5,6,5,7,5]
x=int(input('x='))
while x in L:
    L.remove(x)   
print(L)