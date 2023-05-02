def tokenize(s):
    token1=[]
    token2=""
    for i in range(len(s)):
        if s[i].isspace():
            continue
        elif s[i] in"+-*/^()":  # các kí tự toán học
            if len(token2)>0:
                token1.append(token2)
                token2=""
            token1.append(s[i])
        else:
            token2+=s[i]
    if len(token2)>0:
        token1.append(token2)
    return token1
def main():
    n=input("Nhap chuoi: ")
    token1=tokenize(n)
    print(token1)
main()