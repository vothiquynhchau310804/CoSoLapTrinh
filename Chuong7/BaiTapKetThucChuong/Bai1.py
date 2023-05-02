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
            hoa+=1
        elif st[i].islower():
            thuong+=1
        elif st[i].isnumeric():
            so+=1
        else:
            khac+=1
    return hoa,thuong,so,khac
def InKQ(hoa,thuong,so,khac):
    print('In hoa:',hoa)
    print('In thuong:',thuong) 
    print('Chu so:',so)
    print('Khac:',khac)       
st=Input()
hoa,thuong,so,khac=XuLy(st)
InKQ(hoa,thuong,so,khac)