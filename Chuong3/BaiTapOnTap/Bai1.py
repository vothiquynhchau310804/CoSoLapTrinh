n=int(input('n='))
if n>=0 and n<=100:
    if n==0:
        print('n!=0')
    else:
        giaithua=1
        i=1
        while i<=n:
            giaithua*=i
            i+=1
        print('{0}!={1}'.format(n,giaithua))

        
            