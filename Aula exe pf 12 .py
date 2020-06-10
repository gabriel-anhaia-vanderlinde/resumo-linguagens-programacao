#12. Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
media = 0
aluno1 = {}
aluno2 = {}
nota = []

aluno1['nome'] = input('Informe o nome do primeiro aluno: ')
aluno1['nota1'] = (float(input('Informe a primeira nota: ')))
aluno1['nota2'] = (float(input('Informe a segunda nota: ')))
aluno1['nota3'] = (float(input('Informe a terceira nota: ')))
aluno1['nota4'] = (float(input('Informe a quarta nota: ')))
nota_gr = aluno1.get('nota1') + aluno1.get('nota2') + aluno1.get('nota3') + aluno1.get('nota4')
aluno1['media'] = nota_gr / 4

aluno2['nome'] = input('Informe o nome do Segundo aluno: ')
aluno2['nota1'] = (float(input('Informe a primeira nota: ')))
aluno2['nota2'] = (float(input('Informe a segunda nota: ')))
aluno2['nota3'] = (float(input('Informe a terceira nota: ')))
aluno2['nota4'] = (float(input('Informe a quarta nota: ')))
nota_gr = aluno2.get('nota1') + aluno2.get('nota2') + aluno2.get('nota3') + aluno2.get('nota4')
aluno2['media'] = nota_gr / 4

alunos.append(aluno1)
alunos.append(aluno2)
print(alunos)
situacao = input('Ver notas individuais dos alunos S/N')
if situacao in 'Ss':
    aluno_r = input('Gostaria de ver a nota de qual aluno, informe (aluno1 ou aluno2)') 
    if aluno_r == aluno1:
        print(f'Nome do aluno: {aluno1["nome"]}, 1º nota : {aluno1["nota1"]}, 2º nota : {aluno1["nota2"]}, 3º nota : {aluno1["nota3"]}, 4º nota : {aluno1["nota4"]}, media :{aluno1["media"]} ')
    else:
        print(f'Nome do aluno: {aluno2["nome"]}, 1º nota : {aluno2["nota1"]}, 2º nota : {aluno2["nota2"]}, 3º nota : {aluno2["nota3"]}, 4º nota : {aluno2["nota4"]}, media :{aluno2["media"]} ')
