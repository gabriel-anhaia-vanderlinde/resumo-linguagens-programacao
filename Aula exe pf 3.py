#3. Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#  já na posição correta de inserção (sem usar o sort()).
#  No final, mostre a lista ordenada na tela.

numeros = []

for count in range(0, 5):
    numero = int(input('Informe um numero: '))

    if count == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero >= numeros[posicao]:
                numeros.insert(posicao, numero)
                break
            posicao += 1

print(numeros)