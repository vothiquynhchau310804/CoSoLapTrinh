#nhap so tu nhien n, tinh tong chu so chan trong n so nhap vao
n=int(input('n='))
sum=0
for i in range(1,n+1):
    x=int(input())
    if x%2==0:
        sum=sum+x
print('tong cac chu so chan la:',sum)