import random
def tao():
    d = []
    v = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    s = ['s', 'h', 'd', 'c']
    for i in v:
        for j in s:
            d.append(i + j)
    return d

def xaotron(d):
    for i in range(len(d)):
        j = random.randint(0, len(d)-1)
        d[i], d[j] = d[j], d[i]
if __name__ == '__main__':
    d = tao()
    print('Truoc khi tron bai:')
    print(d)
    xaotron(d)
    print('Sau khi tron bai:')
    print(d)
