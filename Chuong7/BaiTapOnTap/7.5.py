def Input():
    st=input()
    return st
def Xuly(st):
    chu=0
    so=0
    for i in range(len(st)):
        if st[i].isalpha():
            chu=chu+1
        elif st[i].isnumeric():    
            so=so+1
    return chu,so
def InKQ(chu,so):
    print('Chu cai:',chu)
    print('Chu so:',so)
st=Input()
chu,so=Xuly(st)
InKQ(chu,so)