soam=0
soduong=0
while True:
    n=int(input())
    if n==0:
        break
    elif n<0:
        soam=soam+1
    else:
        soduong=soduong+1
print(soduong,'so duong')
print(soam,'so am')