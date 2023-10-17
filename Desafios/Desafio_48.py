s = 0

for n in range(1,500):
    if n % 3 == 0 and n % 2 != 0 :
        s += n

print('A soma = ', s) 