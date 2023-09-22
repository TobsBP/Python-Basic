altura = float(input("Coloque a altura da parede: "))
largura = float(input("Coloque a largura da parede: "))
area = altura * largura
quant_tinta = area / 2

print("A área da parede = {}".format(area))
print("A quantidade de tinta necessária para pinta a parede = {}".format(quant_tinta))