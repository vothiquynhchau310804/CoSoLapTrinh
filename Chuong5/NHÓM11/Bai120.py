def kiemtrasapxep(L):
    if len(L) <= 1:
        return True
    if L[0] <= L[1]:
        direction = "tang"
    else:
        direction = "giam"
    for i in range(2, len(L)):
        if direction == "tang":
            if L[i] < L[i-1]:
                return False
        elif direction == "giam":
            if L[i] > L[i-1]:
                return False
    return True
L= input("Nhập danh sách các giá trị, cách nhau bằng khoảng trắng: ").split()
L= [int(x) for x in L]
if kiemtrasapxep(L):
    print("Danh sách đã được sắp xếp.")
else:
    print("Danh sách không được sắp xếp.")
