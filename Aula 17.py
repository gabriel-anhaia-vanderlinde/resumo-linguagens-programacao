import random
aluno1 = str(input('Nome do aluno'))
aluno2 = str(input('Nome do aluno'))
aluno3 = str(input('Nome do aluno'))
aluno4 = str(input('Nome do aluno'))
ganhador =[aluno1, aluno2, aluno3, aluno4]
print('O ganhador foi {}'.format(random.choice(ganhador)))