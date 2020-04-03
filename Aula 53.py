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