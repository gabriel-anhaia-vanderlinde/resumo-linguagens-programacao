soma = 0
for count in range(0, 6):
    numero = int(input('Escolha um numero: '))
    if numero % 2 == 0:
        soma += numero
print('A soma é de {}'.format(soma))
