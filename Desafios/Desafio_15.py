km = float(input("Quantidade de km percorridos: "))
days = int(input("Quantidade de dias: "))
carro = 60 * days + 0.15 * km

print("O preço total = R${:.2f}".format(carro))