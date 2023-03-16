KW=int(input('Tieu thu='))
if KW <= 100:
    thanhtien = KW* 550
elif KW <= 150:
    thanhtien = 100 * 550 + (KW - 100) * 750
elif KW <= 200:
    thanhtien = 100 * 550 + 50 * 750 + (KW - 150) * 950
else:
    thanhtien = 100 * 550 + 50 * 750 + 50 * 950 + (KW - 200) * 1350
ThueVAT = thanhtien * 0.1
ThanhtiencoVAT =thanhtien + ThueVAT
print("Phai tra=",ThanhtiencoVAT,sep='')