jogador = dict()

jogador['nome'] = input('Informe o nome do jogador ')
jogador['qtd_jogos']  = int(input('Informe a quantidade de partidas que ele jogou: '))
gols = list()

for i in range(0, jogador.get('qtd_jogos')):
    gols.append(int(input(f'Informe a quantidade de gols para a {i + 1}º')))

jogador['gols'] = gols
jogador['total_gols'] = sum(gols)

print(jogador)