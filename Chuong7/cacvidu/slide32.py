def Input():
    st1=input('st1=')
    st2=input('st2=')
    st3=input('st3=')
    return st1,st2,st3
def checkstring(st1,st2,st3):
    if st1.startswith(st2) or st1.endswith(st3):
        return True
    else:
        return False
st1,st2,st3=Input()
kq=checkstring(st1,st2,st3)
print(kq)
