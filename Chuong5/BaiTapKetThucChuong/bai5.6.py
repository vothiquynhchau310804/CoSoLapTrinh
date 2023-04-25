def Input():
    A=[]
    for i in range(10):
        x=int(input())
        A.append(x)
    return A
def HoanDoi(A):
    B=[]
    for i in range(0,len(A)-1,2):
        B.append(A[i+1])
        B.append(A[i])
    for i in B:
        print(i,end=' ')      
A=Input()
HoanDoi(A)