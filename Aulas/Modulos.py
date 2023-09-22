from math import sqrt, floor
import random
import emoji
num = 10

print("Raiz = {}".format(sqrt(num)))
print("Raiz arredondada para baixo = {}".format(floor(sqrt(num))))
print("Número aleatorio entre 1 e 10:", random.randint(1, 10))
print("Teste do emoji", emoji.emojize("Olá, mundo :sun:"))

#Caso queria importar algo em expecifico use from nome da biblioteca import oq deseja