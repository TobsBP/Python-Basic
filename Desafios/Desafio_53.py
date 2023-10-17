word = str(input('Digite uma palavra: '))
word_reverse = word[::-1]

if word == word_reverse:
    print('São iguais')
else:
    print('São diferentes')