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
soma = 0
for count in range(0, 6):
    numero = int(input('Escolha um numero: '))
    if numero % 2 == 0:
        soma += numero
print('A soma é de {}'.format(soma))
/////////////////////////
peso1 = float(input('Informe o peso da pessoa: '))
peso2 = float(input('Informe o peso da pessoa: '))
peso3 = float(input('Informe o peso da pessoa: '))
peso4 = float(input('Informe o peso da pessoa: '))
peso5 = float(input('Informe o peso da pessoa: '))
print('O maior peso foi de {}'.format(max(peso1, peso2, peso3, peso4, peso5)))
print('O menor peso foi de {}'.format(min(peso1, peso2, peso3, peso4, peso5)))
/////////////////////////
nota = float(input('Digite um valor valido'))
while nota > 10 or nota < 0:
    nota = float(input('Valor não é valido, digite outro valor'))
/////////////////////////
nota_invalida = True
while(nota_invalida):
    nota = float(input('Informe uma nota entre o e 10: '))
    if nota <= 10 and nota >= 0:
        nota_invalida = False

print('NOta registrada é {} '.format(nota))
/////////////////////////
# Desafio FizzBuzz
# Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

# Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
# Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
# Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.

def edivisivel(a, b):
    if a % b == 0:
        return True
    else:
        return False

def fizzbuzz(num):
    if edivisivel(num, 3) and edivisivel(num, 5):
        return 'FizzBuzz'
    elif edivisivel(num, 3):
        return 'Fizz'
    elif edivisivel(num, 5):
        return 'Buzz'
    else:
      return num
     

assert fizzbuzz(3) == 'Fizz'   
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(9) == 'Fizz'

assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(10) == 'Buzz'

assert fizzbuzz(15) == 'FizzBuzz'
assert fizzbuzz(30) == 'FizzBuzz'
assert fizzbuzz(11) == 11
        
assert edivisivel(4, 2) == True
assert edivisivel(5, 2) == False

for i in range(1, 100 + 1):
    fb = fizzbuzz(i)
    print(fb)



    

  
print('Teste OK!')
/////////////////////////
usuario_senha_invalidos = True

while usuario_senha_invalidos:
    usuario = input('Informe um nome de usuario')
    senha = input('informe uma senha diferente ')
    if usuario == senha:
        print('Informe uma senha ou usuario diferente: ')
    else:
        print('Seu usuario e senha foram cadastrados, bem vindo {} '.format(usuario))
        usuario_senha_invalidos = False
/////////////////////////
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
/////////////////////////
#upondo que a população de um país A seja da ordem de 80000 habitantes
#com uma taxa anual de crescimento de 3% e que a população de B 
#seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
#que calcule e escreva o número de anos necessários para que a população do
#país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a = 80000
pop_b = 200000
anos = 0
cres_a = 0.03
cres_b = 0.015
while (pop_a < pop_b):
    anos += 1
    pop_a = pop_a + (pop_a * cres_a)
    pop_b = pop_b + (pop_b * cres_b)
print("Após {} anos o país A ultrapassou o país B em número de habitantes.".format(anos))
print("País A: {}".format(int(pop_a)))
print("País B: {}".format(int(pop_b)))
/////////////////////////
populacoes = True
while populacoes: 
    pop_a = int(input('informe a população da cidade A: '))
    pop_b = int(input('informe a população da cidade B: '))
    anos = 0
    cres_a = float(input('informe a taxa de crescimento da população da cidade A: '))
    cres_b = float(input('informe a taxa de crescimento da população da cidade B: '))
    while (pop_a < pop_b):
        anos += 1
        pop_a = pop_a + (pop_a * cres_a)
        pop_b = pop_b + (pop_b * cres_b)
        if pop_a > pop_b:
            print("Após {} ano(s) o país A ultrapassara o país B em número de habitantes.".format(anos))
            print("País A: {}".format(int(pop_a)))
            print("País B: {}".format(int(pop_b)))
        else:
            print('Após {} ano(s) a cidade A ainda não atingiu ou superou a quantidade de habitantes da cidade B'.format(anos))
    escolha = input('Quer fazer uma contagem relacionando as populações? S/N :')
    if escolha == 'N' or escolha == 'n':
        break
/////////////////////////
nomes = ('gabriel', 'joao', 'pedro')

for i, valor in enumerate(nomes):
    print('o valor {} esta na posicão {} da tupla'.format(valor, i))
/////////////////////////
from random import randint

numeros = (randint(0, 100),randint(0, 100),randint(0, 100),randint(0, 100),randint(0, 100))
print(numeros)

maior = 0
menor = 0

for index, valor in enumerate(numeros):
    if index == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print('o maior valor é {}'.format(maior))
print('o menor valor é {}'.format(menor))
/////////////////////////
numero = int(input('Informe um numero: '))

for count in range(1, 11):
    soma = numero * count
    print('{} * {} = {}. '.format(numero, count, soma))
/////////////////////////
valores = (
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
    int(input('Informe um valor: ')),
)

qnt_9 = 0
index_de3 = None
for valor in valores:
    if valor == 9:
        qnt_9 = qnt_9 + 1

print('Foi encontrado {} noves entre esses valores'.format(qnt_9))
if 3 in valores:
    print('Foi encontrado o numero três na posição {}'.format(valores.index(3)))
else:
    print('Não foi encontrado nenhum três na lista')

for valor in valores:
    if valor % 2 == 0:
        print('Numero par {}'.format(valor))
/////////////////////////
lista = ('Feijão','5,00', 'Arroz', '3,99', 'Macarrão', '2,50')
print('''
o {} , está custando {}.
o {} , está custando {}.
o {} , está custando {}.
'''.format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5]))
/////////////////////////

palavras = ('caixa', 'veneno', 'bebida', 'carregador', 'diametro')

for palavra in palavras:
    print('A palavra {}, possui as segintes vogais: '.format(palavra), end='')
    for letra in palavra:
        if letra in 'aeiou':
            print('{} ,'.format(letra), end='')
    print()
/////////////////////////
lista = []
for valor in range(5):
    valor = int(input('numero: '))
    lista.append(valor)

maior = max(lista)
menor = min(lista)
maior_index = lista.index(maior)
menor_index = lista.index(menor)
print(lista)
print('O Maior número é {}, estando na poseição {}.\n O Menor número é {}, estando na poseção {} .'.format(maior,maior_index,menor,menor_index))
/////////////////////////
continuar_adicionando_numeros = True
listas_de_numeros = []
while continuar_adicionando_numeros:
    numero = int(input('informe um numero: '))

    if numero in listas_de_numeros:
        print('Esse valor ja se encontra na lista')
    else:
        listas_de_numeros.append(numero)
        print('Valor Adiciona a lista')

    decisao = input('Deseja continuar informando outros números? . S/N ')
    if decisao in 'Nn':
        continuar_adicionando_numeros = False

    

listas_de_numeros.sort()
print(listas_de_numeros)
/////////////////////////
numeros = []

for count in range(0, 5):
    numero = int(input('Informe um numero: '))

    if count == 0 or numero > numeros[-1]:
        numeros.append(numero)
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero >= numeros[posicao]:
                numeros.insert(posicao, numero)
                break
            posicao += 1

print(numeros)
/////////////////////////
lista = []

while True:
    numero = int(input('Informe um número: '))
    lista.append(numero)

    decisao = input('Deseja continuar adicionando outros números: S/N ')
    if decisao in 'Nn':
        break

print(lista)
print('{} numeros listados. '.format(len(lista)))
lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('O valor 5 está na lista e se encontra na posução {}')
else:
    print('o valor 5 não se encontra na lista. ')
/////////////////////////
lista = []
lista_par = []
lista_impar = []
while True:
    numero = int(input('Informe um número: '))
    lista.append(numero)

    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
    
    decisao = input('Deseja continuar adicionando outros números: S/N ')
    if decisao in 'Nn':
        break

print(lista)
print('Numeros pares: {}'.format(lista_par))
print('Numeros impares: {}'.format(lista_impar))
/////////////////////////
#FUNÇÃO 1
def funcao1(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


n = int(input('Digite um número: '))
funcao1(n)

#FUNÇÃO 2
def funcao2(n):
    x = 1
    while x <= n:
        y = 1
        piramide = ''
        while y <= x:
            piramide += str(y) + ', '
            y += 1
        print (piramide)
        x += 1


n = int(input('Digite um número: '))
funcao2(n)

#FUNÇÃO 3
def funcao3():
    valor1 = int(input('Informe um valor: '))
    valor2 = int(input('Informe um valor: '))
    valor3 = int(input('Informe um valor: '))


    soma = valor1 + valor2 + valor3
    print(soma)
funcao3()

#FUNÇÃO 4
def funcao4(n):
    if n >= 0:
        print('O número é positivo(P)')
    else:
        print('O número é negativo(N)')


n = int(input('Informe um numero: '))
funcao4(n)

#FUNÇÃO 
def somalImposto(taxaImposto, custo):
    porce_1 = custo /100
    imposto = taxaImposto * porce_1
    valor_final = custo + imposto
    print(f'O valor do produto com impostos é de {valor_final}')



taxaImposto = float(input('Informe a porcentagem do imposto:'))
custo = float(input('Informe o custo do produto'))
somalImposto(taxaImposto, custo)
/////////////////////////
#1. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

from random import randint

numeros = (randint(0, 100),randint(0, 100),randint(0, 100),randint(0, 100),randint(0, 100))
print(numeros)

maior = 0
menor = 0

for index, valor in enumerate(numeros):
    if index == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print('o maior valor é {}'.format(maior))
print('o menor valor é {}'.format(menor))
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
