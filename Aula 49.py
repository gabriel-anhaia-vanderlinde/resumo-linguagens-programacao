from random import randint

numeros = (randint(0, 100),randint(0, 100),randint(0, 100),randint(0, 100),randint(0, 100))
print(numeros)

maior = 0
menor = 0

for index, valor in enumerate(numeros):
    if index == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print('o maior valor é {}'.format(maior))
print('o menor valor é {}'.format(menor))
