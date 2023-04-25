# def Input():
#     st=input()
def format_list(items):
    """Định dạng danh sách các chuỗi đầu vào theo định dạng chuẩn."""
    n = len(items)
    if n == 0:
        return ""
    elif n == 1:
        return items[0]
    elif n == 2:
        return " and ".join(items)
    else:
        # Nối các phần tử đầu tiên bằng dấu phẩy, sau đó nối phần tử cuối cùng bằng từ "and".
        return ", ".join(items[:-1]) + ", and " + items[-1]

# Ví dụ sử dụng hàm format_list
items = input("Nhập danh sách các phần tử, cách nhau bằng dấu phẩy: ").split(",")
formatted_list = format_list(items)
print("Danh sách đã định dạng:", formatted_list)