n=int(input('n='))
giatri=n
dem=0
if n!=0:
    while n>0:
        n=n//10 #n=int(n/10)
        dem=dem+1
else:
    dem=1  
print(giatri,'co',dem,'chu so')