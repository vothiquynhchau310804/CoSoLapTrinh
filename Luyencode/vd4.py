a=int(input('a='))
b=int(input('b='))
ch=input('toan tu:')
if ch=="+":
    kq=a+b
elif ch=='-':
    kq=a-b
elif ch=='*':
    kq=a*b
elif ch=='/':
    if b==0:
        print('khong hop le')
    else:
        kq=a/b
print('Ket qua phep toan la:',kq)