def Input():
    st=input()
    return st
def XuLy(st):
    hoa=0
    thuong=0
    so=0
    khac=0
    for i in range(len(st)):
        if st[i].isupper():
            hoa=hoa+1
        elif st[i].islower():
            thuong=thuong+1
        elif st[i].isnumeric():
            so=so+1
        else:
            khac=khac+1
    return hoa,thuong,so,khac
def KQ(hoa,thuong,so,khac):
    print('In hoa:',hoa)
    print('In thuong:',thuong)
    print('Chu so:',so)
    print('Khac:',khac)
st=Input()
hoa,thuong,so,khac=XuLy(st)
KQ(hoa,thuong,so,khac)