sentence1="Hi how are you?"
sentence2="Bananas,apples,watermelon"
sentence3=sentence1+" "+sentence2


def count_words(sentence):
    sentence=sentence.replace(':',' ')
    sentence=sentence.replace('.',' ')
    sentence=sentence.replace(',',' ')
    sentence=sentence.replace(';',' ')

    words = sentence.split()
    return len(words)

count=count_words(sentence3)
print(count)


