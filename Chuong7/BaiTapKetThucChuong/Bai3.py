def Input():
    mk=input()
    return mk
def MatKhau(mk):
    a=b=c=d=0
    if len(mk)>=6 and len(mk)<=17:
        for i in mk:
            if 'a' <= i <= 'z':
                a = a + 1
            elif 'A' <= i <= 'Z':
                b = b + 1
            elif '0' <= i <= '9':
                c = c + 1
            elif i=='$' or i=='#' or i=='@':
                d=d+1
        if a > 0 and b > 0 and c > 0 and d>0:
            print(True)
        else:
            print(False)
mk=Input()
MatKhau(mk)