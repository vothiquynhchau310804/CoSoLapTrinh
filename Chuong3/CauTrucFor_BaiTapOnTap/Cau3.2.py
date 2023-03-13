n = int(input("Nhap so nguyen n: "))
a= 0 #số lượng số đã in trên một dòng 
for i in range(1, n+1):
    print(i, end=" ")
    a=a+ 1
    if a == 10:
        print()
        a = 0