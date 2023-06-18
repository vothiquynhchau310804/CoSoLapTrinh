n=int(input())
sum=0
if n==0:
    print('NO')
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
sum=sum%10
if sum==9:
    print('YES')
else:
    print('NO')