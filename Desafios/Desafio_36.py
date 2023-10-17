casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você vai pagar? '))

mensalidade = casa / anos

if mensalidade > salario * 0.30:
    print('\033[31mEmprestimo negado!\033[m')
else:
    print('O valor das parcelas são: R${:.2f}'.format(mensalidade))