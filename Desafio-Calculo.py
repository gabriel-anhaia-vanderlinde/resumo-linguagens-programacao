while not desligar:
    Operacao = int(input("""Escolha qual operação matemática gostaria de fazer :
       [1] Soma
       [2] Subtração
       [3] Divisão
       [4] Multiplicação
       [5] Exponenciação (Segundo número equivale a Exponeciação)
       [6] Radiciação (Segundo número equivale a Radiciação)
       [7] Resto de divisão
          """)
     num1 = int(input('Digite o primeiro número'))
     num2 = int(input('Digite o Segundo número'))
    
    if Operacao = 1:
        resultado := num1 + num2
    elif Operacao == 2:
        resultado := num1 - num2
    elif Operacao == 3:
        resultado := num1 / num2            
    elif Operacao == 4:
        resultado := num1 * num2     
    elif Operacao == 5:
        resultado := num1 ** num2            
    elif Operacao == 6:
        resultado := pow(num1x,1/num2)
    elif Operacao == 7:
        resultado := num1 % num2      


