def Nhap():
    a=int(input("He so cua so can chuyen:"))
    b=input("So can chuyen:")
    c=int(input("He so muon chuyen:"))
    return a,b,c
def doiheso(a,b,c):
    try:
        d=int(b,a)
        s=""
        while d>0:
            cs=d%c
            if cs<10:
                s+=str(cs)
            else:
                s+=chr(ord('A')+cs-10)
            d//=c
        s=s[::-1]
        print(b,"He so",a,"la",s,"trong co so",c)
    except ValueError as e:
        print (e)
def kq():
    if __name__=="main": doiheso()
a,b,c=Nhap()
S=doiheso(a,b,c)
kq()