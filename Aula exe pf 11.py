#11. Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

q_jogos = int(input('Quantos jogos deseja gerar:'))
jogos = []

for i in range(0, q_jogos):
    jogo = []
    while len(jogo) < 6:
        numero = randint(0, 60)
        if numero not in jogo:
            jogo.append(numero)
    jogos.append(jogo)
    
print(jogos)