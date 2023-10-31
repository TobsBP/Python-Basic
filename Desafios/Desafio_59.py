num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

troca = ''
menu = 0

while menu != 5:
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Sair do programa')

    menu = int(input('Escolha uma opção: '))

    if menu == 1:
        print('O valor da soma: {}'.format(num_1 + num_2))
    elif menu == 2:
        print('O valor da subtração: {}'.format(num_1 - num_2))
    elif menu == 3:
        print('O valor da multiplicação: {}'.format(num_1 * num_2))
    elif menu == 4:
        print('O valor da divisão: {}'.format(num_1 / num_2))

    troca = str(input('Deseja trocar os números? (S/N): ')).upper()
    
    if troca == 'S':
        num_1 = int(input('Digite um número: '))
        num_2 = int(input('Digite outro número: '))