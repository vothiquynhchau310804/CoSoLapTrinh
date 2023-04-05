# #nhập số tự nhiên rồi tính tổng 2 chữ số cuối cùng
# n=int(input('n='))
# sum=(n//10)%10+n%10
# print('Tong 2 chu so cuoi la:',sum)


# n = int(input())
# gt=n
# tongcacsochan = 0
# while n > 0:
#     d = n % 10  # Lấy chữ số cuối cùng của n
#     if d % 2 == 0:  # Nếu chữ số là chẵn, cộng vào tổng
#         tongcacsochan += d
#     n //= 10  # Loại bỏ chữ số cuối cùng của n

# # In kết quả
# print("Tổng các chữ số chẵn của", gt, "là:", tongcacsochan)

# nhập từ bàn phím số nguyên n. Nhập liên tục từ bàn phím n số nguyên. tính tổng các chữ số chẵn
# n=int(input('n='))
# tong=0
# for i in range(1,n+1):
#     x=int(input())
#     if x%2==0:
#         tong=tong+x
# print('Tong cua cac so chan la:',tong)
# n=int(input('n='))
# souoc=0
# for i in range(1,n+1):
#     if n%i==0:
#         souoc+=1
# if souoc==2:
#     print(n,'la so nguyen to')
# else:
#     print(n,'khong la so nguyen to')
n=int(input())
iff n<1 or n>50:
    print()
else:
    snt=True
    for i in range(2,n+1)
        for j in range(2,i)
            if i%j ==0
                snt==False
                break
        else:
            print(i,end='')