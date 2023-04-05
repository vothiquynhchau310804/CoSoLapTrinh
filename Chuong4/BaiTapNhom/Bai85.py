# def nhap():
#     n=int(input('Nhap tu 1 den 12: '))
#     return n
# def xuly(n):
#     if n==1:
#         a='first'
#         return a
#     elif n==2:
#         b='second'
#         return b
#     elif n==3:
#         c='third'
#         return c
#     elif n==4:
#         d='fourth'
#         return d
#     elif n==5:
#         e='fifth'
#         return e
#     elif n==6:
#         i='sixth'
#         return i
#     elif n==7:
#         g='seventh'
#         return g
#     elif n==8:
#         h='eighth'
#         return h
#     elif n==9:
#         k='ninth'
#         return k
#     elif n==10:
#         l='tenth'
#         return l
#     elif n==11:
#         j='eleventh'
#         return j
#     elif n==12:
#         m='twelfth'
#         return m
#     else:
#         s='Khong hop le'
#         return s
# def inkq(kq):
#     print(kq)   
# n=nhap()
# kq=xuly(n)
# inkq(kq)     


def ordinalNumber(num):
    if num == 1:
        return "first"
    elif num == 2:
        return "second"
    elif num == 3:
        return "third"
    elif num == 4:
        return "fourth"
    elif num == 5:
        return "fifth"
    elif num == 6:
        return "sixth"
    elif num == 7:
        return "seventh"
    elif num == 8:
        return "eighth"
    elif num == 9:
        return "ninth"
    elif num == 10:
        return "tenth"
    elif num == 11:
        return "eleventh"
    elif num == 12:
        return "twelfth"
    else:
        return ""

# Display each integer from 1 to 12 and its ordinal number
for i in range(1, 13):
    print(str(i) + " = " + ordinalNumber(i))