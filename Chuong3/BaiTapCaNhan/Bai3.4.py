T=int(input())
L=int(input())
H=int(input())
ĐTB=(T*2+H+L*3)/6
if ĐTB<3:
    print('Kem')
elif ĐTB<5:
    print('Yeu')
elif ĐTB<6:
    print('Trung binh')
elif ĐTB<7:
    print("Trung binh Kha")
elif ĐTB<8:
    print('Kha')
elif ĐTB<9:
    print('Gioi')
else:
    print('Xuat sac')