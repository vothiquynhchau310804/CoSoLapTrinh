x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+':
    K=round(x+y,1)
    print(x,'+',y,'=',K,sep='')
elif ch=='-':
    K=round(x-y,1)
    print(x,'-',y,'=',K,sep='')
elif ch=='*':
    K=round(x*y,1)
    print(x,'*',y,'=',K,sep='')
elif ch=='/':
    if y==0:
        print('Khong hop le')
    else:
        K=round(x/y,1)
        print(x,'/',y,'=',K,sep='')
else:
    print('Khong hop le')