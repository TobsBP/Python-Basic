i = 0
soma = 0
maior = -1
menor = 999999

print('Digite os números')
num = int(input('Número = '))

while num != 999:
    soma += num    
    i += 1
    if num < menor:
        menor = num
    elif num > maior:
        maior = num
    num = int(input('Número = '))

print('Média: {:.2f}'.format(soma / i))
print('Menor número: {}'.format(menor))
print('Maior número: {}'.format(maior))