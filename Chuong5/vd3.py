l=[1,3,2,3,4,3,5]
x=int(input('x='))
if x in l:
    del(l[l.index(x)])
    # while x in l:
    #     l.remove(x)
    # while l.count(x)>0:
    #     l.remove(x)
else:
    l.append(x)
print(l)
