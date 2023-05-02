def remove_outliers(L, n):
    if len(L) < 4:
        print("loi: Nhap it nhat 4 gia tri")
        return L
    L.sort()
    L= L[n:-n]
    return L
L= [4, 2, 7, 1, 9, 5, 8, 3, 6]
n = 2
new_L= remove_outliers(L, n)
print("new_L:",new_L)
print("L:",L)


