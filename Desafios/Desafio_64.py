i = 0
soma = 0

print('Digite os números')
num = int(input('Número = '))

while num != 999:
    soma += num    
    i += 1
    num = int(input('Número = '))

print('A soma dos números digitados foi de {}'.format(soma))
print('Foram digitado(s): {}'.format(i))