def Nhap():
    s=input()
    return s
def Viethoa(s):
    ch=s.replace('i','I')
    if len(s)>0:
        ch=ch[0].upper()+ch[1:]
    x=0
    while x<len(s):
        if ch[x]=='.' or ch[x]=='!' or ch[x]==',' or ch[x]=='?':
            x=x+1
            while x<len(s) and ch[x]==' ':
                x+=1
            if x<len(s):
                ch = ch[0:x] + ch[x].upper() + ch[x+1:]
        x+=1
    return ch
def InKQ(kq):
    print(kq)
s=input()
kq=Viethoa(s)
print(kq)