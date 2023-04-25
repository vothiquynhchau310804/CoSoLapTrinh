def find_sublists(list):
    sublists = []
    for i in range(len(list)):
        for j in range(i+1, len(list)+1):
            sublists.append(list[i:j])
    return sublists

list = [1, 2, 3, 4]
sublists = find_sublists(list)
print("Các danh sách con của", list, "là:", sublists)
