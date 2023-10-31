from random import randint

attempt = 0
num = randint(0,10)

print('Tente acertar o número que eu pensei!!')
test = int(input('Digite o número que você acha que é: '))

while test != num:
    attempt += 1
    test = int(input('Você errou! Tente novamente: '))

print('Parabéns, foram {} tentativas.'.format(attempt))