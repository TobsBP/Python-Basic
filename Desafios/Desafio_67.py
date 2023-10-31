num = int(input('Digite o número que deseja ver a tabuada: '))
cont = 0

while True:
    if num < 0:
        break

    texto = f'Tabuada do {num}'.format(num)
    print('-'*50)
    print('{:^50}'.format(texto))
    print('-'*50)

    for i in range(1,11):
        print(f'{num} * {i} = {num * i}')

    cont += 1
    
    num = int(input('Digite o número que deseja ver a tabuada: '))