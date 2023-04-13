def Nhap():
    n=input()
    return n
def vietHoa(n):
    chu=n.replace('i','I')
    if len(n)>0:
        chu=chu[0].upper()+chu[1:]
    x=0
    while x<len(n):
        if chu[x]=='.' or chu[x]=='!' or chu[x]==',' or chu[x]=='?':
            x=x+1
            while x<len(n) and chu[x]==' ':
                x+=1
            if x<len(n):
                chu = chu[0:x] + chu[x].upper() + chu[x+1:]
        x+=1
    return chu
def InKQ(kq):
    print(kq)
n=input()
kq=vietHoa(n)
print(kq)