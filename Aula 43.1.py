nota_invalida = True
while(nota_invalida):
    nota = float(input('Informe uma nota entre o e 10: '))
    if nota <= 10 and nota >= 0:
        nota_invalida = False

print('NOta registrada é {} '.format(nota))