def Nhap():
    a=str(input())
    b=int(input())
    return a,b
def Xuly(a,b):
    if len(a)<b:
        daucach=int((b-len(a))/2)  #lấy số nguyên
        if daucach<=1:
            return a
        else:
            b=' '*daucach+a
            return b
    else:
        return a
a,b=Nhap()
print(Xuly(a,b))