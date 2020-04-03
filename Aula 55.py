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