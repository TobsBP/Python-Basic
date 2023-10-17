num = int(input("Digite o número no qual deseja a tabuada: "))

for mult in range(1,10):
    print('{} * {} = {}'.format(num, mult, num * mult))