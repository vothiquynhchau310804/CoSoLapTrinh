import math
print("Nhap hai canh ke cua tam giac vuong:")
a =int(input()) 
b = int(input()) 
c=math.sqrt(a**2+b**2)
print("Canh ke thu nhat la: ",a,", canh ke thu hai: " ,b,", co canh huyen = ", round(c,2),sep='')