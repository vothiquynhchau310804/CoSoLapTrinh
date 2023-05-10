def Input():
    st=input().strip()
    return st
def XuLy(st):
    st=st.lower()
    st=st.split()
    st=' '.join(st)
    st=st.capitalize()
    st=st.replace(' ,',',').replace(' ;',';').replace(' .','.').replace(' :',':')
    print(st)
st=Input()
XuLy(st)