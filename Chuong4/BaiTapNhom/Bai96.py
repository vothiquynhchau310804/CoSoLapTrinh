def nhap():
    n=input('Password: ')
    return n
def xuly(n):
    x=y=z=0
    if len(n)>= 8:
        for i in n:
            if '0' <= i <= '9':
                x = x + 1
            elif 'A' <= i <= 'Z':
                z = z + 1            
            elif 'a' <= i <= 'z':
                z = z + 1
        if x > 0 and y > 0 and z > 0:
            print('TRUE')
        else:
            print('FALSE')
    else:
        print('khong hop le')
n=nhap()
xuly(n)
# def nhap():
#     n = input('Password: ')
#     return n

# def xuly(n):
#     x = y = z = 0
#     if len(n) >= 8:
#         for i in n:
#             if 'a' <= i <= 'z':
#                 x = x + 1
#             elif 'A' <= i <= 'Z':
#                 y = y + 1
#             elif '0' <= i <= '9':
#                 z = z + 1
#         if x > 0 and y > 0 and z > 0:
#             print('TRUE')
#         else:
#             print('FALSE')
#     else:
#         print('Mật khẩu phải có ít nhất 8 ký tự')

# n = nhap()
# xuly(n)

