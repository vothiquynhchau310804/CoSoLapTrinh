def nhap():
    toantu=input('Nhap toan tu: ')
    return toantu
def precedence(toantu):
    # if toantu=='+'or toantu=='-' or toantu=='*' or toantu=='/':
    if toantu=='+' or toantu=='-':
        print('1')
    elif toantu=='*' or toantu=='/':
        print('2')
    elif toantu=='^':
        print('3')
    else:
        print('-1')
toantu=nhap()
precedence(toantu)