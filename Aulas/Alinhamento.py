nome = str(input("Qual é o seu nome? "))

# Alinha para direita {:>}
print("Prazer em te conhecer {:>20}!".format(nome))

# Alinha para esquerda {:<}
print("Prazer em te conhecer {:<20}!".format(nome))

# Centraliza {:^}
print("Prazer em te conhecer {:^20}!".format(nome))

# Centraliza com decoração {:=^}
print("Prazer em te conhecer {:=^20}!".format(nome))

# end=' ' não quebra a linha no final
# \n quebra a linha