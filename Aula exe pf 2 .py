#2.Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


continuar_adicionando_numeros = True
listas_de_numeros = []
while continuar_adicionando_numeros:
    numero = int(input('informe um numero: '))

    if numero in listas_de_numeros:
        print('Esse valor ja se encontra na lista')
    else:
        listas_de_numeros.append(numero)
        print('Valor Adiciona a lista')

    decisao = input('Deseja continuar informando outros números? . S/N ')
    if decisao in 'Nn':
        continuar_adicionando_numeros = False

listas_de_numeros.sort()
print(listas_de_numeros)