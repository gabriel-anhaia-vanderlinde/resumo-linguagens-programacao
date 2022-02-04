valor = int(input('Quanto dinheiro você tem em R$?'))
valorcv = valor / 4.39
print('Em Dolar seu dinheiro de R${}, é equivalente a ${} hoje.'.format(valor, valorcv))
/////////////////////////
Largura = float(input('Informe a largura da parede'))
Altura = float(input('Informe a altura da parede'))
Litros = Largura*Altura / 2
print('Uma parede com Largura {} e Altura {}, necessita de {} litros de tinta para pintar a parede'.format(Largura, Altura, Litros))
/////////////////////////
Valor = float(input('Valor do Produto?'))
Desconto = Valor - Valor*(0.05)
print('O produto custa R${} com desconto de 5% o pruduto custará R${}'.format(Valor, Desconto))
/////////////////////////
nota1 = float(input('Primeira Nota'))
nota2 = float(input('Segunda Nota'))
media = (nota1+nota2)/2
print('media do aluno igual a {}'.format(media))
if(media >=7) :
    print('Aprovado')
else: 
    print('Reprovado')
/////////////////////////
nm1 = int(input('Escolha um número'))
dobro = nm1 * 2
triplo = nm1 * 3
raiz = float(nm1) ** 0.5
print('O número {} tem como dobro {}, como Triplo {}, e sua raiz é {}'.format(nm1, dobro, triplo, raiz ))
/////////////////////////
nm1 =int(input('Digite um numero'))
nma = nm1 - 1
nmd = nm1 + 1
print('O numero {} tem com Antessesoro número {} e seu Sucessor como {}'.format(nm1, nma, nmd))
/////////////////////////
nome = input("Qual o seu nome? ")
print('Seja bem vindo {}!.'.format (nome))
/////////////////////////
nm1 = int(input('DIgite um Número'))
nm2 = int(input('Digite outro Número'))
soma = nm1 + nm2
print('soma de {} e {} é igual a {}'.format(nm1, nm2, soma))
/////////////////////////
nomeber = input('Digite um Numero')
print('O tipo primitivo é', type(nomeber))
print('Tem espaços?', nomeber.isspace())
print('É um número?', nomeber.isnumeric())
print('É alfabetico?', nomeber.isalpha())
print('É alfanúmerico?', nomeber.isalnum())
print('É maisculo?', nomeber.isupper())
print('É minusculo?', nomeber.islower())
print('É capitalizado?', nomeber.istitle())

/////////////////////////
Numero = float(input('Qual o número?'))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 0, Numero*0))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 1, Numero*1))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 2, Numero*2))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 3, Numero*3))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 4, Numero*4))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 5, Numero*5))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 6, Numero*6))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 7, Numero*7))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 8, Numero*8))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 9, Numero*9))
print('O numero {}, multiplicado por {}, é igual a {}'.format(Numero, 10, Numero*10))


/////////////////////////
salario = float(input('Salário do trabalhador?'))
aumento = salario + salario*0.15
print('O novo salario com o aumento é de {}'.format(aumento))
/////////////////////////
Numero = float(input('Informe um número'))
print(int(Numero))
/////////////////////////
catetoad = float(input('Informe o cateto adjacente'))
catetoop = float(input('Informe o cateto oposto'))
hipotequ = catetoad*catetoad + catetoop*catetoop
hipotefi = hipotequ**0.5
print('A hipotenusa equivale a {}'.format(hipotefi))
/////////////////////////
import math
ang = float(input('digite o ângulo que você deseja.'))
seno = math.sin(math.radians(ang))
print('seno : {: .2}'.format(seno))
cosseno = math.cos(math.radians(ang))
print('cosseno : {: .2}'.format(cosseno))
tangente = math.tan(math.radians(ang))
print('tangente : {: .2}'.format(tangente))
/////////////////////////
import random
aluno1 = str(input('Nome do aluno'))
aluno2 = str(input('Nome do aluno'))
aluno3 = str(input('Nome do aluno'))
aluno4 = str(input('Nome do aluno'))
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('Sorteio:',alunos)
/////////////////////////
import random
aluno1 = str(input('Nome do aluno'))
aluno2 = str(input('Nome do aluno'))
aluno3 = str(input('Nome do aluno'))
aluno4 = str(input('Nome do aluno'))
ganhador =[aluno1, aluno2, aluno3, aluno4]
print('O ganhador foi {}'.format(random.choice(ganhador)))
/////////////////////////
velocidade = int(input('Velocidade do Carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80 :
    print('Você ultrapassou o limite permitido, será mutado em R${}' .format(multa))
else:
    print('Você esta numa velocidade correta, prossiga e uma boa viagem. ')
/////////////////////////
Numero = int(input('Digite um Numero: '))
if Numero %2:
    print('è impar ')
else:
    print('È par ')
/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////
