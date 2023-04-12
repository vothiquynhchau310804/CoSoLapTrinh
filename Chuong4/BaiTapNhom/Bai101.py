#rut gon mot phan so thanh so hang nho nhat
# gcd: ước chung lớn nhất
def nhap():
    a=int(input('Tu so='))
    b=int(input('Mau so='))
    return a,b
def uocChungLonNhat(a,b):
    c=min(a,b)
    gcd=1
    for i in range(1,c+1):
        if a%i==0 and b%i==0:
            gcd=i   
    return gcd
def rutGonPhanSo(a,b,gcd):
    if a==0:
        return 0,1
    else:
        tuMoi=a//gcd
        mauMoi=b//gcd
        return tuMoi,mauMoi
def inKQ(tuMoi,mauMoi):
    print('Phan so rut gon la: ',tuMoi,'/',mauMoi,sep='')
a,b=nhap()
gcd=uocChungLonNhat(a,b)
tuMoi,mauMoi=rutGonPhanSo(a,b,gcd)
inKQ(tuMoi,mauMoi)

