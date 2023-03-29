n = int(input("n="))
i = 1  
while i <= n:
    print(i, end=" ")
    if i%10 == 0:
        print()  
    i=i+1 