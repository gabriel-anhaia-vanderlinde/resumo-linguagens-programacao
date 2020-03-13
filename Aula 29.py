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