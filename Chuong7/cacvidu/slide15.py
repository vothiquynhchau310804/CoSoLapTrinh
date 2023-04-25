# while True:
#     st1=input('st1=')
#     st2=input('st2=')
#     if st2 in st1:
#         print('Nhap lai')
#         break
while True:
  st1 = input("Nhập vào một xâu ký tự: ")
  st2 = input("Nhập vào một xâu cần kiểm tra: ")
  
  if st2 in st1:
    print("Xâu st2 xuất hiện trong xâu st1. Vui lòng thử lại.")
  else:
    print("Xâu st2 không xuất hiện trong xâu st1.")
    break
