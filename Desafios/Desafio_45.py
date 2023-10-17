import random
jogadas = ['Pedra', 'Tesoura', 'Papel']
jogadas = random.choice(jogadas)

player = str(input('Escolha, Pedra, Papel, Tesoura\n'))

if jogadas == player:
    print('Jogada do pc: {}.'.format(jogadas))
    print('Empate.')
elif jogadas == 'Pedra' and player == 'Papel':
    print('Jogada do pc: {}.'.format(jogadas))
    print('Você ganhou!!')
elif jogadas == 'Pedra' and player == 'Tesoura':
    print('Jogada do pc: {}.'.format(jogadas))
    print('Você perdeu!!')
elif jogadas == 'Tesoura' and player == 'Papel':
    print('Jogada do pc: {}.'.format(jogadas))
    print('Você perdeu!!')
elif jogadas == 'Tesoura' and player == 'Pedra':
    print('Jogada do pc: {}.'.format(jogadas))
    print('Você ganhou!!')
elif jogadas == 'Papel' and player == 'Pedra':
    print('Jogada do pc: {}.'.format(jogadas))
    print('Você perdeu!!')
elif jogadas == 'Papel' and player == 'Tesoura':
    print('Jogada do pc: {}.'.format(jogadas))
    print('Você ganhou!!')