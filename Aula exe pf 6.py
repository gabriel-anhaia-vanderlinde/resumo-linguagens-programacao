#6.Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista_de_expressao = []
expressao = input('Digite uma expressão utilizando parênteses')

for c in expressao:
    if c == '(':
        lista_de_expressao.append(c)
    elif c == ')':
        if len(lista_de_expressao) > 0:
            lista_de_expressao.pop()
        else:
            lista_de_expressao.append(c)
            break
if len(lista_de_expressao) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta')
