tuoinguoi=int(input('Nhap tuoi nguoi: '))
if tuoinguoi <0:
    print('Khong hop le')
else:
    if tuoinguoi<=2:
        tuoicho=tuoinguoi*10.5
    else:
        tuoicho=2*10.5
        tuoicho=tuoicho+(tuoinguoi-2)*4
print("Tuoi cua con nguoi la",tuoinguoi, "tuoi bang tuoi cua", round(tuoicho,1), "nam cho.")