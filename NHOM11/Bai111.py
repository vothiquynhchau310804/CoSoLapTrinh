#tách từng từ trong câu có sẵn
L=[".",",","?","!","-",":",";"]
a=input("Nhap chuoi:")
a+=" "
for i in range(len(L)):
    a=a.replace(L[i],"")
#tách từ
b=a.split()
print(b)