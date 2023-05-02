def Input():
    st=input().split(',')
    return st
def XuLy(st):
    i=0
    while i< len(st):
        if st.count(st[i])>1:
            st.remove(st[i])
        else:
            i=i+1
    st.sort()
    st=','.join(st)
    print(st)
st=Input()
XuLy(st)