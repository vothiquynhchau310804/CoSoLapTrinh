# n = int(input())  #nhập giá trị n
# while n >= 0:
#     if n == 0:
#         print("0!=1")
#         n = int(input())
#     else:
#         giaithua = 1
#         i = 1
#         while i <= n:
#             giaithua =giaithua*i
#             i=i+1
#         print(giaithua)
#         n = int(input())

while True:
    n=int(input())
    if n==0:
        print('1')
    elif n>0:
        giaithua=1
        i=1
        while i<=n:
            giaithua*=i
            i=i+1
        print(giaithua)
    else:
        break