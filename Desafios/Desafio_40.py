nota1 = int(input('Nota 1 = '))
nota2 = int(input('Nota 2 = '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado!!')
elif media >= 5 and media < 7:
    print('Recuperação.')
elif media >= 7:
    print('Aprovado!!!')