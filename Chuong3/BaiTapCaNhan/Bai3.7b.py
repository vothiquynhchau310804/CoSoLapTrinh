# n=int(input())
# while n>=0:
#     if n==0:
#         print('0!=1')
#         n=int(input())
#     else:
#         giaithua=1
#         for i in range(1,n+1):
#             giaithua=giaithua*i
#         print(giaithua)
#         n=int(input())
while True:
    n=int(input())
    if n==0:
        print('1')
    elif n>0:
        giaithua=1
        for i in range(1,n+1):
            giaithua*=i
        print(giaithua)
    else:
        break
        
