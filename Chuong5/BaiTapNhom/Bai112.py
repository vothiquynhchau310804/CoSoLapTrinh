def Nhap():
    DuoiTB=[]
    BangTB=[]
    TrenTB=[]
    L=[]
    while True:
        n=input()
        if n=="":
            break
        L.append(float(n))    
    return L,DuoiTB,BangTB,TrenTB
def TinhTB(L):
    TB=sum(L)/len(L)
    for i in range(len(L)):
        if L[i]<TB:
            DuoiTB.append(L[i])
        elif L[i]==TB:
            BangTB.append(L[i]) 
        else: TrenTB.append(L[i])
    return TB
def InKQ():
    print("TB:",TB)
    print("DuoiTB:",DuoiTB)
    print("BangTB:",BangTB)
    print("TrenTB:",TrenTB)
L,DuoiTB,BangTB,TrenTB=Nhap()
TB=TinhTB(L)
InKQ()