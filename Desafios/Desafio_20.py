import random

aluno_1 = input("Digite o nome do aluno 1: ")
aluno_2 = input("Digite o nome do aluno 2: ")
aluno_3 = input("Digite o nome do aluno 3: ")
aluno_4 = input("Digite o nome do aluno 4: ")
alunos = [aluno_1,aluno_2,aluno_3,aluno_4]

random.shuffle(alunos)

print("A ordem dos alunos:" , alunos)