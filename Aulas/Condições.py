nome = str(input('Qual o seu nome? '))
if nome == 'Tobias':
    print('Que nome lindo {}'.format(nome))
else:
    print('Boa noite {}'.format(nome)) 

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media > 6:
    print('A dupla pegou média!')
else:
    print('A dupla não pegou média...')