# # # Hàm chuyển đổi từ năm người sang năm chó
# # def human_to_dog_age(human_age):
# #     # Kiểm tra năm người nhập vào là số dương
# #     if human_age < 0:
# #         return "Lỗi: Năm người không thể là số âm!"
# #     # Nếu năm người nhỏ hơn hoặc bằng 2 năm, tính theo cách tính này
# #     elif human_age <= 2:
# #         dog_age = human_age * 10.5
# #     # Nếu năm người lớn hơn 2, tính theo cách tính này
# #     else:
# #         dog_age = 21 + (human_age - 2) * 4
# #     return dog_age

# # # Nhập năm người từ bàn phím
# # human_age = float(input("Mời bạn nhập năm tuổi của người: "))
# # # Chuyển đổi từ năm người sang năm chó và in ra màn hình
# # dog_age = human_to_dog_age(human_age)
# # print("Năm tuổi của người tương đương với", dog_age, "năm tuổi của chó")
# Bài tập 1: Xác định tên của hình từ số cạnh


# python

# Copy code
# # Hàm xác định tên của hình từ số cạnh của nó
# def name_of_polygon(num_of_sides):
#     # Kiểm tra số cạnh nhập vào có nằm trong khoảng cho phép không
#     if num_of_sides < 3 or num_of_sides > 10:
#         return "Lỗi: Số cạnh của hình phải từ 3 đến 10!"
#     # Xác định tên của hình từ số cạnh và trả về tên đó
#     elif num_of_sides == 3:
#         return "Tam giác"
#     elif num_of_sides == 4:
#         return "Tứ giác"
#     elif num_of_sides == 5:
#         return "Ngũ giác"
#     elif num_of_sides == 6:
#         return "Lục giác"
#     elif num_of_sides == 7:
#         return "Thất giác"
#     elif num_of_sides == 8:
#         return "Bát giác"
#     elif num_of_sides == 9:
#         return "Cửu giác"
#     elif num_of_sides == 10:
#         return "Thập giác"

# # Nhập số cạnh của hình từ bàn phím
# num_of_sides = int(input("Mời bạn nhập số cạnh của hình: "))
# # Xác định tên của hình và in ra màn hình
# polygon_name = name_of_polygon(num_of_sides)
# print("Hình có", num_of_sides, "cạnh là", polygon_name)

# Bài tập 2: Tên tháng đến số ngày


# python

# Copy code
# # Hàm xác định số ngày trong tháng từ tên tháng nhập vào
# def days_in_month(month_name):
#     # Chuyển tên tháng về chữ thường để chống trùng lặp không cần thiết
#     month_name = month_name.lower()
#     # Xác định số ngày trong tháng và trả về số đó
#     if month_name == "tháng 1" or month_name == "tháng một":
#         return 31
#     elif month_name == "tháng 2" or month_name == "tháng hai":
#         return "28 hoặc 29"
#     elif month_name == "tháng 3" or month_name == "tháng ba":
#         return 31
#     elif month_name == "tháng 4" or month_name == "tháng tư":
#         return 30
#     elif month_name == "tháng 5" or month_name == "tháng năm":
#         return 31
#     elif month_name == "tháng 6" or month_name == "tháng sáu":
#         return 30
#     elif month_name == "tháng 7" or month_name == "tháng bảy":
#         return 31
#     elif month_name == "tháng 8" or month_name == "tháng tám":
#         return 31
#     elif month_name == "tháng 9" or month_name == "tháng chín":
#         return 30
#     elif month_name == "tháng 10" or month_name == "tháng mười":
#         return 31
#     elif month_name == "tháng 11" or month_name == "tháng mười một":
#         return 30
#     elif month_name == "tháng 12" or month_name == "tháng mười hai":
#         return 31
#     else:
#         return "Lỗi: Tên tháng không hợp lệ!"

# # Nhập tên tháng từ bàn phím
# month_name = input("Mời bạn nhập tên tháng: ")
# # Xác định số ngày trong tháng và in ra màn hình
# num_of_days = days_in_month(month_name)
# print("Tháng", month_name, "có", num_of_days, "ngày")

# Bài tập 3: Cường độ âm thanh


# python

# Copy code
# # Hàm xác định tiếng ồn tương ứng với mức độ âm thanh tính bằng đề-xi-ben
# def sound_level(decibel):
#     # Xác định tiếng ồn tương ứng với mức độ âm thanh và trả về tên đó
#     if decibel >= 130:
#         return "Búa khoan"
#     elif decibel >= 106:
#         return "Máy cắt cỏ chạy xăng"
#     elif decibel >= 70:
#         return "Đồng hồ báo thức"
#     elif decibel >= 40:
#         return "Căn phòng im ắng"
#     else:
#         return "Lỗi: Mức độ âm thanh không hợp lệ!"

# # Nhập mức độ âm thanh tính bằng đề-xi-ben từ bàn phím
# decibel = float(input("Mời bạn nhập mức độ âm thanh tính bằng đề-xi-ben: "))
# # Xác định tiếng ồn tương ứng và in ra màn hình
# sound_name = sound_level(decibel)
# print("Với mức độ âm thanh là", decibel, "đề-xi-ben, tương ứng với tiếng ồn của", so
# Bài tập 40: Phân loại tam giác


# python

# Copy code
# # Hàm phân loại tam giác từ độ dài 3 cạnh
# def triangle_type(side1, side2, side3):
#     # Kiểm tra xem 3 cạnh có tạo thành tam giác được không
#     if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
#         return "Lỗi: 3 cạnh này không phải là 3 cạnh của tam giác!"
#     # Phân loại tam giác dựa trên độ dài các cạnh
#     elif side1 == side2 == side3:
#         return "Tam giác

