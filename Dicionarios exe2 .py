
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    'jogador1' : randint(1, 6),
    'jogador2' : randint(1, 6),
    'jogador3' : randint(1, 6),
    'jogador4' : randint(1, 6),
}

for key, value in jogadores.items():
    print(f'O {key} acertou o número {value} no dado')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('='*30)

for count, value in enumerate(ranking):
    print(f'{count + 1}º lugar, {value[0]} que conseguiu o numero {value[1]} no dado')
