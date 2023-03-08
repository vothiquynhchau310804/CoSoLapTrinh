import math
a=int(input("Nhap do dai canh a: "))
b=int(input("Nhap do dai canh b: "))
c=int(input("Nhap do dai canh c: "))
s=(a+b+c)/2
Dt=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Dien tich=",Dt)