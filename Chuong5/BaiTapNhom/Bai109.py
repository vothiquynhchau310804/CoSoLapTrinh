def Nhap():
    n=int(input("n="))
    return n
def TimUoc(n):
    L=[]
    for i in range (1,n+1):
        if n%i==0:
            L=L+[i]
    return L
def InKQ(L,n):
    print("Danh sach uoc cua",n,":")
    for i in range (len(L)):
        print(L[i], end=", ")

n=Nhap()
L=TimUoc(n)
InKQ(L,n)