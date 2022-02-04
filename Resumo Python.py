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
valormetro =float(input('Informe o valor'))
valorcentimetro = valormetro * 100
valormilimetro = valormetro * 1000
print('O valor de {} metros, em centimetros é {} e em milimetros {}'.format(valormetro, valorcentimetro, valormilimetro ))
/////////////////////////
Ano = int(input('Digite o ano: '))
if Ano % 4:
    print('Não é bissesto')
else:
    print('È bissesto')
/////////////////////////

N1 = int(input('Digite Um numero: '))
N2 = int(input('Digite Um numero: '))
N3 = int(input('Digite Um numero: '))
print('o maior numero é',max(N1, N2, N3))
print('o menor numero é',min(N1, N2, N3))
/////////////////////////
salario = float(input('indique o salário'))
aum1251 = salario *0.10
aum1250 = salario *0.15
if salario > 1250:
    print('O aumento do salário foi de R${}. '.format(aum1251))
else:
    print('O aumento de salário foi de R${}. '.format(aum1250))
/////////////////////////
l1 = float(input('Digite o valor da reta: '))
l2 = float(input('Digite o valor da reta: '))
l3 = float(input('Digite o valor da reta: '))
if l1==l2 or l2==l3:
    print('è possivel criar um triângulo')
else:
    print('não é possível criar um triângulo')
/////////////////////////
salario = float(input('Informe o salário: '))
valor = float(input('Informe o valor da casa: '))
anos = 12 * int(input('Informe em quantos anos íra pagar: '))
salario30 = salario *0.30
tempo =  anos / valor
if salario30 >= tempo:
    print('Seu emprestimo foi aprovado, Parabéns.')
else:
    print('Seu emprestimo foi reprovado.')
/////////////////////////
numero = int(input('Digite um Número: '))
print(''' Escolha a conversão do seu número
[1] para binário
[2] para octal
[3] para hexadecimal
''')
escolha = int(input('faça sua escolha '))
if escolha == 1:
    print('Seu número {} foi convertido em {} '.format(numero, bin(numero)[2 :]))
elif escolha == 2:
    print('Seu número {} foi convertido em {} '.format(numero, oct(numero)[2 :]))
elif escolha == 3:
    print('Seu número {} foi convertido em {} '.format(numero, hex(numero)[2 :]))
else :
    print('nada')
/////////////////////////
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro é maior')
elif n2 > n1:
    print('O segundo é maior')
else:
    print('Ambos são iguais')
/////////////////////////
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
/////////////////////////
nota1 = float(input('Informe a nota: '))
nota2 = float(input('Informe a outra nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Reprovado')
elif media >= 7.0:
    print('Aprovado')
else:
    print('Recuperação')
/////////////////////////
reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda da reta: '))
reta3 = float(input('Informe o valor da terceira da reta: '))
if reta1 == reta2 and reta2 == reta3:
    print('É Equilatero')
elif reta1 == reta2 and reta2 != reta3:
    print('É isosceles')
elif reta1 != reta2 and reta2 == reta3:
    print('É isosceles')
elif reta1 == reta3 and reta2 != reta1:
    print('É isosceles')
else:
    print('É Escaleno')
/////////////////////////
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >=18.5 and imc < 25:
    print('Peso Ideal')
elif imc >=25 and imc < 30:
    print('Sobrepeso')
elif imc >=30 and imc <40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')
else:
    print('sksks')
/////////////////////////
valor = float(input('Digite o valor do produto'))
forma_de_p = int(input('''
DIgite 1 para pagamento a vista com cartão ou boleto, 
Digite 2 para pagar a vista com cartão,
Digite 3 para pagamento em duas vezes no cartão,
Digite 4 para pagamento em treê vezes ou mais no cartão:  
'''))
pag_vdc = valor - (valor * 0.10)
pag_cc = valor - (valor * 0.05)
pag_dv = valor
pag_3vm = valor + (valor * 0.2)

if forma_de_p == 1:
    print('O valor pago sera de {}'.format(pag_vdc))
elif forma_de_p == 2:
    print('O valor pago sera de {}'.format(pag_cc))
elif forma_de_p == 3:
    print('O valor pago sera de {}'.format(pag_dv))
elif forma_de_p == 4:
    print('O valor pago sera de {}'.format(pag_3vm))
else:
    print('Algo está errado')     
/////////////////////////
from random import randint
opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
0 para Pedra;
1 para Papel;
2 para Tesoura;
''')
jogador = int(input('Informe sua escolha: '))
print('a escolha do computador foi: {}'.format(opcoes[computador]))
print('a ecolha do jogador foi: {}'.format(opcoes[jogador]))
if computador == 0:
    if jogador == 0:
        print('empatou')
    elif jogador == 1:
        print('Parabéns você conseguir ganhar, bora outra ta com medo??')
    elif jogador == 2:
        print('Parabéns você perdeu kkkk')

elif computador == 1:
    if jogador == 0:
        print('Parabéns você perdeu kkkk')
    elif jogador == 1:
        print('empatou')
    elif jogador == 2:
        print('Parabéns você conseguir ganhar, bora outra ta com medo??')

elif computador == 2:
    if jogador == 0:
        print('Parabéns você conseguir ganhar, bora outra ta com medo??')
    elif jogador == 1:
        print('Parabéns você perdeu kkkk')
    elif jogador == 2:
        print('empatou')
/////////////////////////
from time import sleep

for count in range  (10, 0, -1):
    print('Contagem regressiva {}'.format(count))
    sleep(1)
print('Fogos')
sleep(1)
print('Cabo')
/////////////////////////
for count in range(0, 51, 2):
    print('N {}'.format(count))
/////////////////////////
soma = 0
for count in range(0, 501):
    if count % 3 == 0:
        soma += count
print('A soma é de {}'.format(soma))
/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////

/////////////////////////
