def KiemTraMK():
    while True:
        mk=input()
        if (len(mk)>=8) and any(i.isnumeric() for i in mk) and any(i.isupper() for i in mk) and any(i.islower() for i in mk):
            print('Hop le')
            break
        # else:
        #     # print('Khong hop le')
        #     continue
matkhau=KiemTraMK()