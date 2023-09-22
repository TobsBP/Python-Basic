import math

ang = float(input("Digite o ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))

print("Seno: {:.2f} \nCosseno: {:.2f}" .format(sen, cos))