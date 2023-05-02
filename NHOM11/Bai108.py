L= []
zero = 0  
duong = []
while True:
    x= input("Nhập số nguyên: ")
    if x== "":
        break
    n= int(x)
    if n< 0:
        L.append(n)
    elif n== 0:
        zero += 1
    else:
        duong.append(n)
for n in L + [0]*zero + duong:
    print(n)
