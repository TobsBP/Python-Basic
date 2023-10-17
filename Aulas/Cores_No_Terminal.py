print('\033[4;30;45mOlá mundo!!\033[m')
print('\033[0;33;44mOlá mundo!!\033[m')

a = 5
b = 1
print('Os valores são \033[31m{}\033[m e \033[35m{}\033[m'.format(a, b))

core = {
    'Limpa':'\033[m',
    'Azul':'\033[34m',
    'PretoeBranco':'\033[7;30m',
    'Amarelo':'\033[33m',
    'sublinhadoazul':'\033[4;34m',
    }

nome = 'Tobias'

print('Olá {}{}{}!!'.format(core['sublinhadoazul'], nome, core['Limpa']))