#8. Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
pares = []
impares = []
for count in range(0, 7):
    numero = int(input('informe um número:'))
    #verifica-se se é par 
    if numero %2 == 0:
        pares.append(numero)
    else: 
        impares.append(numero)

pares.sort
impares.sort
lista_todos_os_numeros = pares + impares
impares_pares = [pares, impares]
print('Lista de pares: {}'.format(pares))
print('Lista de impares: {}'.format(impares))
print('Lista de todos os número {}'.format(lista_todos_os_numeros))
print(impares_pares)