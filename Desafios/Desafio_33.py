num_1 = int(input('Número: '))
num_2 = int(input('Número: '))
num_3 = int(input('Número: '))

if num_1 > num_2 and num_1 > num_3:
    print('O maior número é: {}'.format(num_1))
if num_2 > num_1 and num_2 > num_3:
    print('O maior número é: {}'.format(num_2))
if num_3 > num_1 and num_3 > num_2:
    print('O maior número é: {}'.format(num_3))

if num_1 < num_2 and num_1 < num_3:
    print('O menor número é: {}'.format(num_1))
if num_2 < num_1 and num_2 < num_3:
    print('O menor número é: {}'.format(num_2))
if num_3 < num_1 and num_3 < num_2:
    print('O menor número é: {}'.format(num_3))