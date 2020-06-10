
pessoas = []
pessoa = {}
total_idade = 0

while True:
    pessoa['nome'] = input('Infome o nome da pessoa: ')
    pessoa['idade'] = int(input('Informe a idade da pessoa: '))
    pessoa['sexo'] = input('Informe o sexo da pessoa M/F/O: ')
    total_idade += pessoa.get('idade')
    pessoas.append(pessoa.copy())
    pessoa.clear()

    decisao = input('Deseja continar cadastrando? S/N')
    if decisao in 'Nn':
        break

qtd_pessoas = len(pessoas)
media = total_idade / qtd_pessoas
mulheres = []
pessoas_idade_acima_da_media = []

for pessoa in pessoa:
    total_idade += pessoa.get('idade')
    if pessoa.get('sexo') in 'Ff':
        mulheres.append(pessoa)
    if pessoa.get('idade') > media:
        pessoas_idade_acima_da_media.append(pessoa)

print(f'A quantidade de pessoas cadastradas é : {len(pessoas)}')
print(f'A média de idade é: {media} ')
print(f'A lista de mulheres cadastrados foi de {len(mulheres)}, são as seguintes: ')
for mulher in mulheres:
    print(f' Nome: {mulher.get("nome")}, idade: {mulher.get("idade")}')