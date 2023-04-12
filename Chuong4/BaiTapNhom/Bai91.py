def nhap():
    toantu=input('Nhap toan tu: ')
    return toantu
def xuly(toantu):
    if toantu=='+' or toantu=='-':
        print('1')
    elif toantu=='*' or toantu=='/':
        print('2')
    elif toantu=='^':
        print('3')
    else:
        print('-1')
toantu=nhap()
xuly(toantu)