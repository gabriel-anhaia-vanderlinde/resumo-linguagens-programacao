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
    print('O valor 5 está na lista e se encontra na posução {}')
else:
    print('o valor 5 não se encontra na lista. ')