giacoban=4
giatangthem=0.25/0.14
def quangduong():
    s=float(input('So quang duong di duoc la: '))
    return s
def tonggiave(s):
    t=giacoban+giatangthem*s
    return t
def inkq(t):
    print('Tong gia ve la:$',round(t,2),sep='')
s=quangduong()
t=tonggiave(s)
inkq(t)