frase = str(input('Frase: '))
print('A letra (A) aparece: {} vezes.'.format(frase.upper().count('A')))
print('A letra (A) aparece na posição: {}'.format(frase.upper().find('A')))
print('A letra (A) aparece a ultima vez na posição: {}'.format(frase.upper().rfind('A')))