from random import randint
numero_pc = randint(0,5)

print('Tente adivinhar o número que eu escolhi, entre 0 e 5.')
num_adv = int(input('DIgite o número que você acha que eu escolhi: '))

if numero_pc == num_adv:
    print('Parabéns você acertou!!')
else:
    print('Você errou...')