total = 0
caro = 0 
barato = 999999

while True:
    
    nome = str(input('Nome do produto: '))
    preco = int(input('Valor do produto: '))
    keep = str(input('Deseja continuar? (S/N) ')).upper()

    total += preco

    if preco > 1000:
        caro += 1
    if preco < barato:
        barato = preco
        nome_bar = nome

    if keep == 'N':
        break

print(f'O total da compra foi de R${total}')
print(f'{caro} Produtos custaram mais que R$1000.00')
print(f'{nome_bar} foi o produto mais barato no valor de R${barato}')