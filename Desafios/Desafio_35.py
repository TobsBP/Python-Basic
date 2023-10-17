reta_1 = int(input('Digite o tamanho da reta: '))
reta_2 = int(input('Digite o tamanho da reta: '))
reta_3 = int(input('Digite o tamanho da reta: '))

if reta_1 + reta_2 > reta_3 and reta_1 + reta_3 > reta_2 and reta_2 + reta_3 > reta_1:
    print('Sim, essas retas podem formar um triângulo.')
else:
    print('Não, essas retas não podem formar um triângulo.')