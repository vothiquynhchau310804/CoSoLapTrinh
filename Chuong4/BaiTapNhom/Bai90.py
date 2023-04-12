def isInteger(str):
    str=str.strip()
    if str[0] in ("-", "+"):
        return True
    return False

str=input("Nhap chuoi: ")
if isInteger(str):
    print("Cac ky tu trong chuoi dai dien cho mot so nguyen hop le .")
else:
    print("Cac ky tu trong chuoi khong dai dien cho mot so nguyen hop le .")