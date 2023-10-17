a = int(input('Digite o valor do lado do triângulo: '))
b = int(input('Digite o valor do lado do triângulo: '))
c = int(input('Digite o valor do lado do triângulo: '))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print('É um triângulo equilátero.')
    if a == b and b != c:
        print('É um triângulo isósceles.')
    if a != b and b != c and a != c:
        print('É um triângulo escaleno.')
else:
    print('Não é um triângulo.')