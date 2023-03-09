n = int(input("Nhap so nguyen n (1 <= n <= 50): "))
while n < 1 or n > 50:
    n = int(input("So n khong thuoc mien tren. Yeu cau nhap lai:"))
print("Bạn đã nhập số n =",n)