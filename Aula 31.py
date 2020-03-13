nasc = int(input('Informe sua data de nascimento '))
ano = int(input('Informe o ano em que vc está'))
idade = ano - nasc
dtidade = 18 - idade
if idade > 18:
    print('Você está com seu alistamento atrasado.')
elif idade < 18:
    print('Você não precisa se alistar agora, apenas daqui {} ano(s).'.format(dtidade))
else:
    print('Você deve se alistar esse ano. ')