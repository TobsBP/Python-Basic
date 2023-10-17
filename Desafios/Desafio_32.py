ano = int(input('Digite quantos dias tem seu ano: '))

if ano % 366 == 0:
    print('O ano é bixesto.')
else: 
    print('O ano não é bixesto.')