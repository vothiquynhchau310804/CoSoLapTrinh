L=[]
for i in range(10):
    n=int(input())
    L=L+[n]
x=int(input('Nhap vao gia tri x: '))
# for j in L:
#     if L[j]==5:
#         L[j]=x
i=0
while i<len(L):
    if L[i]==5:
        L[i]=x
    i=i+1
print('Ket qua:',L)
    