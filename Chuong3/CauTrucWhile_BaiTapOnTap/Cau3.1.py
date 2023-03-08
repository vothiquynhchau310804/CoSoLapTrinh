while True: #để lặp vô hạn cho đến khi người dùng nhập giá trị hợp lệ.
    n = int(input("Nhap so nguyen n (1<=n<=50): "))
    if n<1 or n>50:
        print("So n khong thuoc mien tren. Yeu cau nhap lai.")
    else:
        break #sử dụng break để thoát khỏi vòng lặp.
print("Ban da nhap so n = ",n)