nome_invalido = True
while nome_invalido:
    nome = input('Informe seu nome: ')
    if len(nome) > 3:
        print('nome confere')
        nome_invalido = False
    else:
        print('Informe um nome valido')

idade_invalida = True
while idade_invalida:
    idade = int(input('Informe sua idade: '))
    if idade >= 0 and idade <=150:
        print('idade confere')
        idade_invalida = False
    else:
        print('Digite uma idade valida:')

salario_invalido = True
while salario_invalido:
    salario = float(input('Informe seu salario: '))
    if salario > 0:
        print('salario confere')
        salario_invalido = False
    else:
        print('Digite um salario valido:')

sexo_invalido = True
while sexo_invalido:
    sexo = input('informe seu sexo, coloque (F) para femenino e (M) para masculino: ')
    if sexo == 'F' or sexo == 'M':
        print('sexo confere')
        sexo_invalido = False
    else:
        print('Digite um sexo valido:')

estado_civil_invalido = True
while estado_civil_invalido:
    estado_civil = input('Informe seu estado civil, coloque (s) para solteiro(a), (c) para casado(a), (v) para viuvo(a) e (d) para divorciado :  ')
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        print('estado civil confere')
        estado_civil_invalido = False
    else:
      print('Digite um estado civil valido:')
    
print('''
Formulario:
Nome: {}
Idade: {}
Salario: {}
Sexo: {}
Estado Civil : {}
'''.format(nome, idade, salario, sexo, estado_civil))
