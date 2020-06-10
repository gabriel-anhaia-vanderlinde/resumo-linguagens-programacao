#7. Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

continuar_informando_valor = True
pessoas = []
pessoa_de_maior_peso = []
pessoa_de_menor_peso = []
while continuar_informando_valor:
    dados_da_pessoa = []
    dados_da_pessoa.append(input('Informe os nomes: '))
    dados_da_pessoa.append(float(input('Informe o peso: ')))

    if len(pessoas) == 0:
        pessoa_de_maior_peso = dados_da_pessoa
        pessoa_de_menor_peso = dados_da_pessoa
    else:
        if dados_da_pessoa[1] > pessoa_de_maior_peso[1]: 
            pessoa_de_maior_peso= dados_da_pessoa
        if dados_da_pessoa[1] < pessoa_de_menor_peso[1]:
            pessoa_de_menor_peso= dados_da_pessoa

    pessoas.append(dados_da_pessoa)
    escolha = input('Você gostaria de continuar adicionando nomes e pesos: S/N ')
    if escolha in 'Nn':
        continuar_informando_valor=False

print(len(pessoas))
print(pessoas)
print(pessoa_de_maior_peso)
print(pessoa_de_menor_peso)
