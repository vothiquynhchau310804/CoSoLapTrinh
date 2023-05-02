def DinhDang(st):
    if len(st)==0:
        return ""
    if len(st)==1:
        return str(st[0])
    ketqua=''
    for i in range(0,len(st)-2):
        ketqua=ketqua+str(st[i])+', '
    ketqua=ketqua+str(st[len(st)-2])+' va '
    ketqua=ketqua+str(st[len(st)-1])
    return ketqua
def XuLy():
    st=[]
    nt=input().strip()
    while nt!='':
        st.append(nt)
        nt=input().strip()
    print('Dinh dang la:',DinhDang(st))
XuLy()