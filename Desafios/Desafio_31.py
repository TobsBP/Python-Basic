km = int(input('Digite a distância em km: '))

if km > 200:
    passagem = 0.45 * km
    print('O preço total das passagens é de: R${:.2f}.'.format(passagem))
else:
    passagem = 0.50 * km
    print('O preço total das passagens é de: R${:.2f}'.format(passagem))