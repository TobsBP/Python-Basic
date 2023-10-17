km = int(input('Digite a velocidade que você passou: '))

if km > 80:
    multa = 7 * (km - 80)
    print('Sua multa é no valor de: R${:.2f}.'.format(multa))
else:
    print('Você não foi multado.')
