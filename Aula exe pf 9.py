#9. Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i,valor in enumerate(matriz): 
    for j, valor in enumerate(matriz[i]):
        matriz[i][j] = input('informe algum valor para linha {} e coluna {}: '.format(i, j))
        print('-='*30)
        for linha in matriz:
            for coluna in linha:
                 print('[ {} ]'.format(coluna), end='')
            print()
        print('-='*30)