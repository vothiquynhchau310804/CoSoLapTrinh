socanh=int(input('Nhap so canh (từ 3 đến 10): '))
if socanh<3 or socanh>10:
    print('Khong hop le. Vui long nhap lai')
else:
    if socanh==3:
        hinh='Tam giac'
    elif socanh==4:
         hinh='Hinh vuong hoac hinh chu nhat'
    elif socanh==5:
        hinh='Ngu giac'
    elif socanh==6:
        hinh='Luc giac'
    elif socanh==7:
        hinh='That giac'
    elif socanh==8:
        hinh='Bat giac'
    elif socanh==9:
        hinh="Cuu giac"
    else:
        hinh='Thap giac'
print('Hinh co',socanh,'canh','la hinh',hinh)