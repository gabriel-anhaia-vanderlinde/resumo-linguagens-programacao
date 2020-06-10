#5. Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
while True:
    numero = int(input('Informe um número: '))
    lista.append(numero)

    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    
    decisao = input('Deseja continuar adicionando outros números: S/N ')
    if decisao in 'Nn':
        break

print(lista)
print('Numeros pares: {}'.format(lista_par))
print('Numeros impares: {}'.format(lista_impar))
