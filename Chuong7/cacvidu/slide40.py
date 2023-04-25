ten=[]
so_luong=[]
for i in range(4):
    T=input("Mat hang: ")
    ten=ten+[T]
    SL=input("So luong: ")
    so_luong=so_luong+[SL]
for i in range (0,4):
    print(ten[i].ljust(20,'.'),end='')
    print(so_luong[i].rjust(7))