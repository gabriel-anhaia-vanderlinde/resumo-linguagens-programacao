
palavras = ('caixa', 'veneno', 'bebida', 'carregador', 'diametro')

for palavra in palavras:
    print('A palavra {}, possui as segintes vogais: '.format(palavra), end='')
    for letra in palavra:
        if letra in 'aeiou':
            print('{} ,'.format(letra), end='')
    print()