num = int(input('Digite um número: '))
e_primo = True

if num <= 1:
    e_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            e_primo = False
            break

if e_primo:
    print('É um número primo.')
else:
    print('Não é um número primo.')
