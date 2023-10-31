while True:

    big = 0
    mens = 0
    wom = 0
    age = int(input('Diga sua idade: '))
    gender = str(input('Diga seu sexo (M/F): ')).upper()
    keep = str(input('Deseja continuar (S/N): ')).upper()

    if age > 18:
        big += 1
    if gender == 'M':
        mens += 1
    if gender == 'F' and age < 20:
        wom += 1
    if keep == 'N':
        break

print(f'Tem {big} maiore(s) de idade.')
print(f'{mens} Homen(s) foram cadastrado(s).')
print(f'Tem {wom} mulhere(s) menore(s) de idade.')