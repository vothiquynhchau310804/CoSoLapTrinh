n=int(input())
tong=0
for i in range(1,n+1):
    tong=tong+i
    if tong>=n+1:
        print(i-1)
        break
