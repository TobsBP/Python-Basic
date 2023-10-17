idade = int(input('Digite sua idade: '))

if idade > 20:
    print('Master')
elif idade <= 20 and idade > 19:
    print('Sênior')
elif idade <= 19 and idade > 14:
    print('Junior')
elif idade <= 14 and idade > 9:
    print('Infantil')
elif idade <= 9:
    print('Mirim')