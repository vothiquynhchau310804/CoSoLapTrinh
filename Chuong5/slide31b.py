L=[]
for i in range(0,10):
    n=int(input())
    L=L+[n]
x=int(input('Nhap vao gia tri x: '))
i=0
while i<len(L):
    if L[i]==x:
        del(L[i])
    i=i+1
print('Sau khi xu ly:',L)