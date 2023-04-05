# import math

# n = int(input("Nhập số nguyên n: "))
# nums = list(map(int, input("Nhập các số nguyên cách nhau bởi dấu cách: ").split()))

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True

# print("Các số nguyên tố là: ", end="")
# for num in nums:
#     if is_prime(num):
#         print(num, end=" ")


import math

n = int(input("Nhập số nguyên n: "))
nums = list(map(int, input(f"Nhập {n} số nguyên cách nhau bởi dấu cách: ").split()))

print("Các số nguyên tố là:")
for num in nums:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)