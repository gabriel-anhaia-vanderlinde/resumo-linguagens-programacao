import random
Numero = [0,1,2,3,4,5]
Sortiado = random.choice(Numero)
Escolha = int(input('Escolha um numero de 0 a 5 '))
if Sortiado == Escolha:
    print('Acertou miseravi!')
else:
    print('se fodeu')