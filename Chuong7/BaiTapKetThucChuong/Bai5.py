def Input():
    st=list(map(int,input().split(' ')))
    s=int(input())
    return st,s
def XuLy(st,s):
    vitri=[]
    for i in range(len(st)):
        if st[i]==s:
            vitri.append(i+1)
            
    if len(vitri)==0:
        print('0')
    else:
        for j in vitri:
            print(j)
            
st,s=Input()
XuLy(st,s)

