def pig_latin(tu):
    nguyenam= "aeiou"
    if tu[0] in nguyenam:
        return tu + "way"
    else:
        for i in range(1, len(tu)):
            if tu[i] in nguyenam:
                return tu[i:] + tu[:i] + "ay"

def translate_sentence(cau):
    b = cau.split()
    L = []
    for tu in b:
        L.append(pig_latin(tu))
    return " ".join(L)
a = input("")
print(translate_sentence(a))