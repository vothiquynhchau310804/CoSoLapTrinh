def pig_latin(word):
    vowels=['a','e','i','o','u']
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if word.lower()[0] in vowels:
        if word[-1] in punctuations:
            word=word[1:-1].capitalize+ word[0].lower()+ 'way' + word[-1]
        else:
            word = word[1:]+word[0].lower() + "way"
        return word
    else:
        if len(word) < 2:
            return word
        if word[-1] in punctuations:
            p = word[-1]
            word = word[:-1]
        else:
            p = ''
        if word[0].isupper():
            word = word[1:].capitalize() + word[0].lower() + 'ay' + p
        else:
            word = word[1:] + word[0] + 'ay' + p
        return word

words = input().split()
pig_latin_result = ' '.join(pig_latin(w) for w in words)
print(pig_latin_result)
