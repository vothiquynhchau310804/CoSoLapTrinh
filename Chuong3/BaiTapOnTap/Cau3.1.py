a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
SLN = a
SBN = a
if b > SLN:
    SLN = b
if c > SLN:
    SLN = c
if b < SBN:
    SBN = b
if c < SBN:
    SBN = c
print("SLN=", SLN,sep='')
print("SBN=", SBN,sep='')