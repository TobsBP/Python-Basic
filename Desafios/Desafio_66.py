print('Digite os números desejados.')
cont = 0
soma = 0

while True:
    num = int(input('Número: '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Soma dos números digitados = {soma}. \nForam digitados {cont}.')