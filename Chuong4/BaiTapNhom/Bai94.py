import random
def taomk():
    mk=''
    n=random.randint(7,10)
    while True:
        i=random.randint(33, 126)
        mk=mk+chr(i)
        if len(mk)==n:
            break
    return mk
def inkq():
    print(mk)

mk=taomk()
inkq()