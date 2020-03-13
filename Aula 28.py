salario = float(input('Informe o salário: '))
valor = float(input('Informe o valor da casa: '))
anos = 12 * int(input('Informe em quantos anos íra pagar: '))
salario30 = salario *0.30
tempo =  anos / valor
if salario30 >= tempo:
    print('Seu emprestimo foi aprovado, Parabéns.')
else:
    print('Seu emprestimo foi reprovado.')