from random import randint

while True:

    cont = 0
    num_pc = randint(1,10)
    num_us = int(input('Diga um valor: '))
    chose = str(input('Você quer par ou impar? (P/I) ')).upper()
    soma = num_pc + num_us

    print(f'Seu número foi {num_us} e o da maquina foi {num_pc}')

    if 2 % soma == 0:
        print(f'A soma deu {soma} ou seja par.')
    else:
        print(f'A soma deu {soma} ou seja ímpar.')

    if 2 % soma == 0 and chose == 'P':
        print('Você ganhou!')
        cont += 1
    elif 2 % soma != 0 and chose == 'I':
        print('Você ganhou!')
        cont += 1
    else:
        print('Eu ganhei!')
        break

    print(f'Você ganhou {cont} jogos!')
    print('Vamos de novo...')