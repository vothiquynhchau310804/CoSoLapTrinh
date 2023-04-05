# numbers=[item for item in range(1,6)]
# print(numbers)

# l=[[x,x+1,x+2] for x in range(1,10,3)]
# print(l)
# print(l[1])
# sv=['an','binh','minh','lan','ngoc']
# print(sv[0])
l=[]
print('Nhap day so:')
while True:
    x=int(input())
    l=l+[x] #thêm một phần tử vào list
    if x==0:
        break
n=int(input('n='))
if n in l:
    print(n,'co ton tai')
else:
    print(n,'khong ton tai')