str=input('str=')
ch=input('ch=')
dem=0
for x in str:
    if x.lower()==ch.lower():
        dem=dem+1
print('Number of character',ch,'is:',dem)