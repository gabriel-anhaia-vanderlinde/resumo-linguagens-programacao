# 7. Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

#continuar_informando_valor = True
#pessoas = []
#while continuar_informando_valor:
    #nome = input('informe os nomes: ')
    #peso = float(input('informe o peso: '))
    #pessoa = []
   # pessoa.append(nome)
   # pessoa.append(peso)
   # pessoas.append(pessoa)
  #  escolha = input('VoçÊ gostaria de continuar adicionadno outros nomes e pesos: S/N')
   # if escolha in 'Nn':
   #     continuar_informando_valor = False

#print(len(pessoas))

# posicionar 3 navios no campo batalha
# 1 vez de cada tentar acertar a posição do advesário.
# acaba quando um jogador destroi todos os navios do adversário.
# import emoji
from random import randint
from time import sleep
import sys

jogo_acabou = False
vez = 'usuario'
pontos_usuario = 0
pontos_computador = 0
tabuleiro = []

#inicializa o tabuleiro
for x in range(0, 8):
    linha = []
    for j in range(0, 8):
        linha.append(None)
    
    tabuleiro.append(linha)

def mostrar_tabuleiro():
    print('\033[34m=-'*20)
    print('\033[31m Pontos do computador: {}'.format(pontos_computador))
    print('\033[32m Seus pontos: {}'.format(pontos_usuario))
    print('\033[34m=-'*20)
    print('    \033[34m0    1    2    3    4    5    6    7\033[m')
    for i, linha in enumerate(tabuleiro):
        print(f'\033[34m{i}', end=' \033[m')

        for j, coluna in enumerate(linha):
            if i <= 3:
                valor_coluna = 'X'
                if coluna != '\033[33m╧\033[m' and coluna is not None:
                    valor_coluna = coluna
                print('\033[31m| {} |'.format(valor_coluna), end='\033[m')
            if i > 3:
                valor_coluna = coluna or 'X'
                print('\033[32m| {} |'.format(valor_coluna), end='\033[m')
        print()

mostrar_tabuleiro()
