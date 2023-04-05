def nhap():
    n=int(input('Nhap so muong cafe: '))
    return n
def xuly(n):
    a=n//3 #canh
    b=n%3 #cafe
    c=a//16 #cốc
    d=a%16 #canhconlai
    print(n,'muong cafe chuyen doi thanh')
    print(c,'coc,',d,'muong canh,',b,'muong cafe')
n=nhap()
xuly(n)
    