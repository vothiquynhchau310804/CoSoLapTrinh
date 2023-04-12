def nhap():
    a=int(input('Thang (tu thang 1 den thang 12): '))
    b=int(input('Nam: '))
    return a,b
def xuly(a,b):
    if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
        print('Thang',a,'nam',b,'co 31 ngay !')
    elif a==4 or a==6 or a==9 or a==11:
        print('Thang',a,'nam',b,'co 30 ngay !')
    elif a==2:
        if b%4==0 and (b%100!=0 or b%400==0):
            print('Thang',a,'nam',b,'co 29 ngay !')
        else:
            print('Thang',a,'nam',b,'co 28 ngay !')           
a,b=nhap()
xuly(a,b)