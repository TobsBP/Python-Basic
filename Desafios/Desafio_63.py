n = int(input('Qual número deseja saber a Sequência de Fibonacci: '))
t1 = 0
t2 = 1
contador = 3

print('{} -> {}'.format(t1,t2), end='')

while contador <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t2 = t3
    t1 = t2
    contador += 1

print(' -> FIM')