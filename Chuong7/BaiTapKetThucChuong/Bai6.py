def Input():
    st=input().split(',')
    return st
def XuLy(st):
    so=[]
    for i in st:
        chuyen=int(i,2)
        if chuyen%3==0:
            so.append(i)
    if len(so)==0:
        print()
    else:
        print(','.join(so))
st=Input()
XuLy(st)