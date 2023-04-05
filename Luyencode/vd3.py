n=int(input('n='))
tongchusochan=0
while n>0:
    d=n%10
    if d%2==0:
        tongchusochan=tongchusochan+d
    n=n//10
print('Tong cac chu so chan la:',tongchusochan)