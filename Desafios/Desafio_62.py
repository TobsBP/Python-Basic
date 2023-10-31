term = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
i = 0

while i < 10:
    prog = term + i * raz
    i += 1
    print(prog)

continuar = int(input('Deseja mais quantos termos: '))

if continuar != 0:
    while i < 10 + continuar:
        prog = term + i * raz
        i += 1
        print(prog)