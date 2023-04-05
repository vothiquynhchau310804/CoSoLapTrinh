#nhap vao 3 so nguyen duong, tim va in ra so lon nhat trong 3 so do
a, b, c=[int(x) for x in input().split()]
max=a
if b>max:
    max=b
if c>max:
    max=c
    
print(max)
