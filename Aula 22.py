velocidade = int(input('Velocidade do Carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80 :
    print('Você ultrapassou o limite permitido, será mutado em R${}' .format(multa))
else:
    print('Você esta numa velocidade correta, prossiga e uma boa viagem. ')