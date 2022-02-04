import math

def PadraoCalculo();
     padrao := int(input(""" Escolha qual tipo de calcúlo gostaria de fazer:
        [1] Calculo entre dois número (Soma Subtração...)
        [2] Tranformação de números (Arrendondamento, Seno, Cosseno...)
    
    """)
    return padrao;
def PadraoCalculo1()
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
        return := num1 + num2
   elif Operacao == 2:
        return := num1 - num2
   elif Operacao == 3:
        return := num1 / num2            
   elif Operacao == 4:
       return := num1 * num2     
   elif Operacao == 5:
       return := num1 ** num2            
   elif Operacao == 6:
       return := pow(num1x,1/num2)
   elif Operacao == 7:
       return := num1 % num2  
  
def PadraoCalculo2()
    Operacao = int(input("""Escolha qual operação matemática gostaria de fazer :
        [1] Arredondamento para Cima
        [2] Arredondamento para Baixo
        [3] Valor Absoluto
        [4] Seno
        [5] Cosseno 
        [6] Tangente
        [7] Converte o ângulo  de radianos para grau
        [8] Converte o ângulo  de graus para radianos
        """)      
        num = int(input('Digite o número))              
        
    if Operacao = 1:
        return := math.ceil(num)
    elif Operacao == 2:
        return := math.floor(num)
    elif Operacao == 3:
        return := math.fabs(num)
    elif Operacao == 4:
        return := math.sin(num)
    elif Operacao == 5:
       return := math.cos(num)
    elif Operacao == 6:
        return := math.tan(num)
    elif Operacao == 7:
        return := math.degrees(num)
    elif Operacao == 8:
        return := math.radians(num)
       
def CalculaNovamente();
    resposta := input('Fazer Novo Caluclo? S/N');
    if  resposta = 'S'
        return true
    else 
        return false 
                        
while not desligar:
    padrao = PadraoCalculo()
    if padrao = 1:
        PadraoCalculo1()
    else if padrao = 2;
        PadraoCalculo2()
    
    CalculaNovamente();        

  
