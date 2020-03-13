salario = float(input('indique o salário'))
aum1251 = salario *0.10
aum1250 = salario *0.15
if salario > 1250:
    print('O aumento do salário foi de R${}. '.format(aum1251))
else:
    print('O aumento de salário foi de R${}. '.format(aum1250))