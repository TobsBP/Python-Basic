frase = 'Curso Em Vídeo Python'
#imprime a 4 letra
print(frase[3])
#imprime da 4 letra até a 13
print(frase[3:13])
#imprime no inicio ate a 13
print(frase[:13])
#imprime apartir do 13 ate o fim
print(frase[13:])
#imprime apartir do 1 ate o 15 de 2 em 2
print(frase[1:15:2])
#para imprimir textos grandes
print("""Tesgnwoignwobnogfowenwogowngowb""")
#para contar a quantidade de letras expecifica
print(frase.count('o'))
#para ver o tamanho da frase
print(len(frase))
#para remover os espaços indesejados
print(frase.strip)
#para trocar palavras
print(frase.replace('Python', 'Android'))
# dividindo
dividido = frase.split()
print(dividido[2][3])