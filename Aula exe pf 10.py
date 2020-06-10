#10. Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. 
# C) O maior valor da segunda linha.

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
soma_pares = 0
coluna3 = 0
maior2linha = 0

def mostrar_matriz():
        print('-='*30)
        for linha in matriz:
            for item in linha:
                 print('[ {} ]'.format(item), end='')
            print()
        print('-='*30)
        print('A soma dos pares é : {}'.format(soma_pares))
        print('-='*30)
        print('a soma da terceira coluna é : {}'.format(coluna3))
        print('-='*30)
        print('o maior valor da segunda linha é {}'.format(maior2linha))
        print('-='*30)
for i,valor in enumerate(matriz): 
    for j, valor in enumerate(matriz[i]):
        matriz[i][j] = int(input('informe algum valor para linha {} e coluna {}: '.format(i, j)))
        if (matriz[i][j] % 2 == 0):
            soma_pares +=  matriz[i][j]

        if (j == 2):
            coluna3 += matriz[i][j]

        if (i == 1):
            if (maior2linha < matriz[i][j]):
                maior2linha = matriz[i][j]

        mostrar_matriz()