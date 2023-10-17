ager = 0
under_age = 0

for i in range(0,7):
    num = int(input('Digite a {}º idade:'.format(i)))
    if num > 21:
        ager += 1
    else:
        under_age += 1

print('Tem {} maiores de idade;\nTem {} menores de idade;'.format(ager, under_age))