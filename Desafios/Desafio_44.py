valor = float(input('Digite o valor do produto: '))
print('Qual a forma de pagamento?')
forma = int(input(' 1- À vista. \n 2- À vista no cartão. \n 3- 2x ou mais no cartão. \n 4- 3x ou mais no cartão.\n'))

if forma == 1:
    valor = valor - valor * 0.10
    print('Valor a pagar R${:.2f}.'.format(valor))
elif forma == 2:
    valor = valor - valor * 0.05
    print('Valor a pagar R${:.2f}.'.format(valor))
elif forma == 3:
    valor = valor / 2
    print('Valor a pagar R${:.2f} duas vezes.'.format(valor))
elif forma == 4:
    valor = valor + valor * 0.20
    print('Valor a pagar R${:.2f}.'.format(valor))