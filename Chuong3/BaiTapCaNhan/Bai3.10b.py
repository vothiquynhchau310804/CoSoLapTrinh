# n = int(input("n="))
# a= 0 #số lượng số đã in trên một dòng 
# for i in range(1, n+1):
#     print(i, end=" ")
#     a=a+ 1
#     if a == 5:
#         print()
#         a = 0
n=int(input('n='))
for i in range(1,n+1):
    print(i,end=' ')
    if i%5==0:
        print()