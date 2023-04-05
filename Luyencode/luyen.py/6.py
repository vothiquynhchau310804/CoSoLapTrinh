#xac dinh xem có phai so chinh phuong khong
import math
n=int(input())
m=math.sqrt(n)
if m==int(m):
    if m*m==n:
        print('YES')
    else:
        print('NO')
else:
    print('NO')