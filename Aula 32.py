nota1 = float(input('Informe a nota: '))
nota2 = float(input('Informe a outra nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Reprovado')
elif media >= 7.0:
    print('Aprovado')
else:
    print('Recuperação')