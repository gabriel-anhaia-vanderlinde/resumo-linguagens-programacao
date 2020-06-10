matriz = []
lista_filha = []
print('Registrando valores em uma matriz: ')
for i in range(0, 3):
    print('Registrando valores a linha {}'.format(i))
    for j in range(0, 3):
        print('Registrando valores a coluna {}'.format(j))
        lista_filha.append(input('Informe um valor para a linha {} e coluna {}:'.format(i, j)))

        matriz.append(lista_filha)
        lista_filha.clear

print(matriz)