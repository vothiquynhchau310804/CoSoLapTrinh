# # Nhập dữ liệu từ bàn phím
# integers = []
# for i in range(10):
#     integer = int(input(f'Nhập vào số nguyên thứ {i+1}: '))
#     integers.append(integer)
# x = int(input('Nhập vào số nguyên x: '))

# # Tìm và thay thế các phần tử có giá trị bằng 5 bằng x
# found = False
# for i in range(len(integers)):
#     if integers[i] == 5:
#         integers[i] = x
#         found = True
# if found:
#     print(f'Mảng sau khi thay thế phần tử có giá trị bằng 5 bằng {x}:')
#     print(integers)
# else:
#     print('Không tìm thấy phần tử có giá trị bằng 5 trong mảng.')

# # Xóa các phần tử có giá trị bằng x
# i = 0
# while i < len(integers):
#     if integers[i] == x:
#         integers.pop(i)
#     else:
#         i += 1
# print(f'Mảng sau khi xóa các phần tử có giá trị bằng {x}:')
# print(integers)
