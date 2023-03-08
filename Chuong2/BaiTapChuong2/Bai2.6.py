hoten=input('Ho ten: ')
Songaycong=int(input('So ngay cong: '))
Dongiangaycong=int(input('Don gia ngay cong: '))
Hesophucap=float(input('He so phu cap: '))
Tamung=int(input('Tam ung: '))
Luong=Dongiangaycong*Songaycong*Hesophucap
Thuclinh=Luong-Tamung
print('Nhan vien',hoten,end=',')
print(' Co tien Luong=',round(Luong,1),end=',',sep='')
print(' Tam ung=',round(Tamung,1),end='',sep='')
print(' va Thuc linh=',round(Thuclinh,1),sep='')