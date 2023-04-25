L=[]
while True:
    word=input()
    if word not in L:
        L.append(word)
    if word=='':
        break
for word in L:
    print(word)