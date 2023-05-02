def Input():
    st1=input('st1=')
    st2=input('st2=')
    st3=input('st3=')
    return st1,st2,st3
def FindAndReplace(st1,st2,st3):
    a=st1.find(st2)
    print('Vi tri xuat hien st2:',a)
    b=st1.replace(st2,st3)
    print('Xau ket qua:',b)
st1,st2,st3=Input()
FindAndReplace(st1,st2,st3)
        