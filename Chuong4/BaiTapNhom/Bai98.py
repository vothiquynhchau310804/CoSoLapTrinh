def hex2int(hex):
    dec = 0
    p = len(hex) - 1
    for i in hex:
        if i.isdigit():
            dec += int(i) * (16 ** p)
        else:
            dec += (ord(i.upper()) - 55) * (16 ** p)
        p -= 1
    return dec

def int2hex(dec):
    if dec < 0 or dec > 15:
        raise ValueError('Gia tri dau vao: ')
    if dec < 10:
        return str(dec)
    else:
        return chr(dec + 55)

def main():
    while True:
        try:
            m = int(input('Nhap 1 de doi he 16 sang 10, 2 de doi he 10 sang 16: '))
            if m not in (1, 2):
                raise ValueError
            break
        except ValueError:
            print('Nhap 1 hoac 2!!!')
    if m == 1:
        while True:
            try:
                hex = input('Nhap so thap luc phan:')
                dec = hex2int(hex)
                break
            except:
                print('Nhap so thap luc phan!!!')
        print('So thap phan cua' ,hex ,'la', dec )
    else:
        while True:
            try:
                dec = int(input('Nhap so thap phan:'))
                hex = int2hex(dec)
                break
            except ValueError as e:
                print(e)
            except:
                print('Nhap so thap phan:')
        print('So thap luc phan cua', dec, 'la', hex)
        
if __name__ == '__main__':
    main()