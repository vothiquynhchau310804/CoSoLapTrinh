def Input():
    thongtin=input()
    return thongtin
def tach(thongtin):
    tach=thongtin.split('Email:')
    email=tach[-1].strip()
    if email=='':
        print()
    else:
        print(email)
thongtin=Input()
tach(thongtin)

    