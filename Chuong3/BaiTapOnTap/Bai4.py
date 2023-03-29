while True:
    a=float(input('a='))
    b=float(input('b='))
    ch=input('Toan tu:')
    if ch=='+':
        K=a+b
        print(a,ch,b,'=',K,sep='')
    elif ch=='-':
        K=a-b
        print(a,ch,b,'=',K,sep='')
    elif ch=='*':
        K=a*b,0
        print(a,ch,b,'=',K,sep='')
    elif ch=='/':
        if b==0:
            print('Khong hop le')
        else:
            K=a/b
            print(a,ch,b,'=',K,sep='')
    else:
        print('Khong hop le')
    m=input('Tiep tuc:')
    if m=='T' or m=='t':
        break