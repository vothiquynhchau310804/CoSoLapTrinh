import random
import string
def Matkhaungaunhien():
    short=7
    long=10
    dem=0
    while True:
        MK = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
        password=''.join(random.choice(MK) for i in range (random.randint(short,long)))
        if Kiemtra(password)==True:
            print("Mat khau cua ban la:",password)
            print("Mat khau tot")
            break
        else:
            dem+=1
            print("Mat khau cua ban la:",password)
            print("Mat khau khong tot")
    print(dem,"lan mat khau khong tot")
    return password
def Kiemtra(password):
    Inhoa = False
    Chuthuong = False
    So = False
    kytudacbiet = False
    for kytu in password:
        if 'a'<= kytu <= 'z':
            Chuthuong = True
        elif kytu >= "A" and kytu <="Z":
            Inhoa = True
        elif kytu >= '0' and kytu <= '9':
            So = True

    if len(password) >=8 and Inhoa and Chuthuong and So and (kytudacbiet==True or kytudacbiet==False):
        return True
    else:
        return False
password=Matkhaungaunhien()
Kiemtra(password)