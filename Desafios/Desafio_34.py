salario = int(input('Digite seu salário: '))

if salario > 1.250:
    aumento = salario + (salario * 0.10)
    print('Seu aumento será no valor de: R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('Seu aumento será no valor de: R${:.2f}'.format(aumento))