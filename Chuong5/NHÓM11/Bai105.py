L=[]
while True:
    n=int(input())
    if n!=0:
        L=L+[n]
    elif n==0:
        break
L.reverse()
L.sort()
for i in range (len(L)):
    print(L[i])