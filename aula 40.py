numero = int(input('Informe um numero: '))

for count in range(1, 11):
    soma = numero * count
    print('{} * {} = {}. '.format(numero, count, soma))