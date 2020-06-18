#FUNÇÃO 1
def funcao1(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


n = int(input('Digite um número: '))
funcao1(n)

#FUNÇÃO 2
def funcao2(n):
    x = 1
    while x <= n:
        y = 1
        piramide = ''
        while y <= x:
            piramide += str(y) + ', '
            y += 1
        print (piramide)
        x += 1


n = int(input('Digite um número: '))
funcao2(n)

#FUNÇÃO 3
def funcao3():
    valor1 = int(input('Informe um valor: '))
    valor2 = int(input('Informe um valor: '))
    valor3 = int(input('Informe um valor: '))


    soma = valor1 + valor2 + valor3
    print(soma)
funcao3()

#FUNÇÃO 4
def funcao4(n):
    if n >= 0:
        print('O número é positivo(P)')
    else:
        print('O número é negativo(N)')


n = int(input('Informe um numero: '))
funcao4(n)

#FUNÇÃO 
def somalImposto(taxaImposto, custo):
    porce_1 = custo /100
    imposto = taxaImposto * porce_1
    valor_final = custo + imposto
    print(f'O valor do produto com impostos é de {valor_final}')



taxaImposto = float(input('Informe a porcentagem do imposto:'))
custo = float(input('Informe o custo do produto'))
somalImposto(taxaImposto, custo)