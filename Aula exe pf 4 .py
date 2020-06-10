#4. Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: 
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    numero = int(input('Informe um número: '))
    lista.append(numero)

    decisao = input('Deseja continuar adicionando outros números: S/N ')
    if decisao in 'Nn':
        break

print(lista)
print('{} numeros listados. '.format(len(lista)))
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('o valor 5 não se encontra na lista. ')