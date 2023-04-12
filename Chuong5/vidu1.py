# # numbers = [item for item in range(5,10)]
# # print(numbers)
# # matrix = [ [x+1,x,x+1,x] for x in range(0,1) ]*3
# # matrix=[ [1,0,1,0] for x in range(1,4) ]
# # print(matrix)
# # myPets = ['Zophie', 'Pooka', 'Fat-tail']
# # print('Enter a pet name:')
# # name = input()
# # if name not in myPets:
# #     print('I do not have a pet named ' + name)
# # else:
# #     print(name + ' is my pet.')
# students=["An","Binh","Lan","Thanh","Minh"]



# #Cach 2
# for x in range(len(students)):
#     print(students[x] ,end=", ")
# # #Cach 1
# for x in students:
#     print(x ,end=", ")
# # #Cach 3
# for x in range(5):
#     print(students[x] ,end=", ")
catNames = [ ]
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1 )+ ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)