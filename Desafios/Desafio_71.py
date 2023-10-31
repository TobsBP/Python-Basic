while True:
    money = int(input('Quanto deseja sacar (ou digite 0 para sair): '))
    
    if money == 0:
        print('Obrigado por usar o caixa eletrônico. Tenha um bom dia!')
        break  # Sai do loop se o usuário digitar 0
    else:
        not_50 = money // 50
        money %= 50

        not_20 = money // 20
        money %= 20

        not_10 = money // 10
        money %= 10

        not_1 = money // 1

        print(f'Total de {not_50} cédulas de R$50')
        print(f'Total de {not_20} cédulas de R$20')
        print(f'Total de {not_10} cédulas de R$10')
        print(f'Total de {not_1} cédulas de R$1')