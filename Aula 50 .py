valores = (
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
)

qnt_9 = 0
index_de3 = None
for valor in valores:
    if valor == 9:
        qnt_9 = qnt_9 + 1

print('Foi encontrado {} noves entre esses valores'.format(qnt_9))
if 3 in valores:
    print('Foi encontrado o numero três na posição {}'.format(valores.index(3)))
else:
    print('Não foi encontrado nenhum três na lista')

for valor in valores:
    if valor % 2 == 0:
        print('Numero par {}'.format(valor))