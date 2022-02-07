
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

################################################  

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
	
################################################  
	
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

################################################  
	
jogador = dict()

jogador['nome'] = input('Informe o nome do jogador ')
jogador['qtd_jogos']  = int(input('Informe a quantidade de partidas que ele jogou: '))
gols = list()

for i in range(0, jogador.get('qtd_jogos')):
    gols.append(int(input(f'Informe a quantidade de gols para a {i + 1}º')))

jogador['gols'] = gols
jogador['total_gols'] = sum(gols)

print(jogador)

################################################  

pessoas = []
pessoa = {}
total_idade = 0

while True:
    pessoa['nome'] = input('Infome o nome da pessoa: ')
    pessoa['idade'] = int(input('Informe a idade da pessoa: '))
    pessoa['sexo'] = input('Informe o sexo da pessoa M/F/O: ')
    total_idade += pessoa.get('idade')
    pessoas.append(pessoa.copy())
    pessoa.clear()

    decisao = input('Deseja continar cadastrando? S/N')
    if decisao in 'Nn':
        break

qtd_pessoas = len(pessoas)
media = total_idade / qtd_pessoas
mulheres = []
pessoas_idade_acima_da_media = []

for pessoa in pessoa:
    total_idade += pessoa.get('idade')
    if pessoa.get('sexo') in 'Ff':
        mulheres.append(pessoa)
    if pessoa.get('idade') > media:
        pessoas_idade_acima_da_media.append(pessoa)

print(f'A quantidade de pessoas cadastradas é : {len(pessoas)}')
print(f'A média de idade é: {media} ')
print(f'A lista de mulheres cadastrados foi de {len(mulheres)}, são as seguintes: ')
for mulher in mulheres:
    print(f' Nome: {mulher.get("nome")}, idade: {mulher.get("idade")}')
