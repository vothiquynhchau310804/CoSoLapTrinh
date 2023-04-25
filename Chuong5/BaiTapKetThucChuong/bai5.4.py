def Input():
    A=[]
    n=int(input('n='))
    for i in range(1,n+1):
        x=int(input())
        A.append(x)
    return A
def DaoNguoc(A):
    A.reverse()  
    return A
def SapXep(A):
    A.sort()
    print(A)
A=Input()
b=DaoNguoc(A)
print(b)
SapXep(A)