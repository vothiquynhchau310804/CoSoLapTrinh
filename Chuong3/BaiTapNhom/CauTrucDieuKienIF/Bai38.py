thang=str(input('Nhap thang: '))
if thang=='1' or thang=='mot' or thang=='3' or thang=='ba' or thang=='5' or thang=='nam' or thang=='7' or thang=='bay' or thang=='8' or thang=='tam' or thang=='10' or thang=='muoi' or thang=='12' or thang=='muoi hai':
    print('Thang',thang,'co 31 ngay')
elif thang=='4' or thang=='tu' or thang=='6' or thang=='sau' or thang=='9'or thang=='chin' or thang=='11' or thang=='muoi mot':
    print('Thang',thang,'co 30 ngay')
elif thang=='2' or thang=='hai':
    nam=int(input('Nam: '))
    if nam%4==0 and nam%100!=0:
        print('Thang',thang,'co 29 ngay')
    else:
        print('Thang',thang,'co 28 ngay')
else:
    print('Khong hop le')