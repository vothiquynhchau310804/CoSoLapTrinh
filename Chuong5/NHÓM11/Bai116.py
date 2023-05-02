def pig_latin(word):
    vowels = "aeiouAEIOU"
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if word[0] in vowels:
        if word[-1] in punctuations:
            new_word = word[1:-1].capitalize() + word[0].lower() + "way" + word[-1]
        else:
            new_word = word[1:].capitalize()+ word[0].lower() + "way"
    else:
        if len(word) < 2:
            new_word = word
        else:
            if word[-1] in punctuations:
                p = word[-1]
                word = word[:-1]
            else:
                p = ''
            if word[0].isupper():
                new_word = word[1:].capitalize() + word[0].lower() + "ay" + p
            else:
                new_word = word[1:] + word[0] + "ay" + p
    return new_word

words = input("Nhap: ").split()
pig_latin_result = ' '.join(pig_latin(w) for w in words)
print(pig_latin_result)
