from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
atual = date.today().year
temp = atual - ano

if temp < 18:
    print('Você ainda vai se alistar, faltam: {} ano(s)'.format(temp))
elif temp > 18:
    temp = temp - 18
    print('Você passou da data de se alistar, foi há: {} ano(s)'.format(temp))
else:
    print('Está na hora de se alistar')