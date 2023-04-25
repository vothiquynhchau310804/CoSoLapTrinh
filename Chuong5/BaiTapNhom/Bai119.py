import random
def chiabaisotay(tay, baitay,bobai):
    taybai = [[] for i in range(tay)]
    for j in range(baitay):
        for i in range(tay):
            taybai[i].append(bobai.pop())
    return taybai
bobai = []
for i in range(1, 14):
    bobai.extend([i]*4)
random.shuffle(bobai)
taybai = chiabaisotay(4, 5, bobai)
for i in range(len(taybai)):
  print("Tay {}: {}".format(i+1, taybai[i]))
print("Số lượng bài còn lại trong bộ bài:", len(bobai))
