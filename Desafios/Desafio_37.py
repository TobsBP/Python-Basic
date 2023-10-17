num = int(input('Digite um número: '))
print('1- Binário\n 2- Octal\n 3- Hexadecimal')
tipo = int(input('Qual tipo de conversão você deseja? '))

if tipo == 1:
    print('O número {} em binário fica: {}'.format(num, bin(num)[2:]))
elif tipo == 2:
    print('O número {} em octal fica: {}'.format(num, oct(num)[2:]))
elif tipo == 3:
    print('O número {} em hexadecimal fica: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!!')