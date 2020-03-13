from random import randint
opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
0 para Pedra;
1 para Papel;
2 para Tesoura;
''')
jogador = int(input('Informe sua escolha: '))
print('a escolha do computador foi: {}'.format(opcoes[computador]))
print('a ecolha do jogador foi: {}'.format(opcoes[jogador]))
if computador == 0:
    if jogador == 0:
        print('empatou')
    elif jogador == 1:
        print('Parabéns você conseguir ganhar, bora outra ta com medo??')
    elif jogador == 2:
        print('Parabéns você perdeu kkkk')

elif computador == 1:
    if jogador == 0:
        print('Parabéns você perdeu kkkk')
    elif jogador == 1:
        print('empatou')
    elif jogador == 2:
        print('Parabéns você conseguir ganhar, bora outra ta com medo??')

elif computador == 2:
    if jogador == 0:
        print('Parabéns você conseguir ganhar, bora outra ta com medo??')
    elif jogador == 1:
        print('Parabéns você perdeu kkkk')
    elif jogador == 2:
        print('empatou')