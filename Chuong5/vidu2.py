#nếu x tồn tại thì xóa, ko tồn tại thì thêm.
L=[1,2,3,4,5]
x=int(input('x='))
i=0
if x in L:
    while i<len(L):
        if L[i]==x:
            del(L[i])
        i=i+1
else:
    L=L+[x]
print('Sau khi xu ly: ')
print(L)