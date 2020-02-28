nota1 = float(input('Primeira Nota'))
nota2 = float(input('Segunda Nota'))
media = (nota1+nota2)/2
print('media do aluno igual a {}'.format(media))
if(media >=7) :
    print('Aprovado')
else: 
    print('Reprovado')