from math import sqrt, pow
cat_op = float(input("Cateto oposto: "))
cat_ad = float(input("Cateto adjacente: "))

hip = sqrt(pow(cat_ad,2) + pow(cat_op,2))

print("A hipotenusa = {:.2f}".format(hip))