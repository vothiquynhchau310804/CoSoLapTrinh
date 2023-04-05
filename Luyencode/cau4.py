
a=int(input())
b=int(input())
c=int(input())
if a>100:
    A=(a-100)*25+b*15+c*20
if a<=100:
    A=b*15+c*20
if a>250:
    B=(a-250)*45+b*35+c*25
if a<=250:
    B=b*35+c*25
print(A)
print(B)