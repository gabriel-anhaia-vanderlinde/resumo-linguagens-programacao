# O sistema de numeração romana (ou números romanos) desenvolveu-se na Roma Antiga e utilizou-se em todo o seu Império.
#  Neste sistema as cifras escrevem-se com determinadas letras, que representam os números. 
# As letras são sempre maiúsculas, já que no alfabeto romano não existem as minúsculas, as letras são I, V, X, L, C, D e M.
# Sua tarefa é desenvolver um programa que converta números indo-arábicos para o formato romano e vice-versa.
#  As regras para a formação dos números romanos são apresentadas a seguir.
# Cada letra corresponde a um determinado valor:
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Agrupando as letras acima, podemos representar os números de acordo com um conjunto de regras:
# Com exceção de V, L e D, os outros numerais podem se repetir no máximo três vezes:
# III = 3
# XXX = 30
# CCC = 300
# MMM = 3000
# Quando escritos à direita de numerais maiores, I, X e C somam-se aos valores dos primeiros:
# VIII = 5 + 1 + 1 + 1 = 8
# LXII = 50 + 10 + 1 + 1 = 62
# CLVIII = 158
# MCXX = 1000 + 100 + 10 + 10 = 1120
# Mas se os numerais I, X e C estiverem à esquerda dos maiores, seus valores são subtraídos como, por exemplo, em:
# IV = 5 - 1 = 4
# IX = 10 - 1 = 9
# XC = 100 - 10 = 90

def converte_para_romando(num):
    num_c = str(num)
    if len(num_c) == 1:
        if num < 4:
            return 'I' * num
        elif num == 4:
            return 'IV'
        elif num > 4 and num < 9:
            num_y = num - 5
            return 'V' + 'I' * num_y
        elif num == 9:
            return 'IX'  
        elif num == 10:
            return 'X'
    elif len(num_c) == 2:
        if num == 10:
                return 'X'  
        elif num > 10 and num < 20:
            num_rt = num_c[1]
            num_y = int(num_rt)
            if num_y > 0 and num_y < 4:
                num_xr = 'I' *num_y
            elif num_y == 4:
                num_xr = 'IV'
            elif num_y >= 6 and num_y < 9:
                num_pt = num - 5
                num_xr = 'V'+ 'I' * num_pt
            elif num_y == 9:
                num_xr = 'IX' 
            return 'X' + num_xr

    


assert converte_para_romando(1) == 'I'
assert converte_para_romando(2) == 'II'
assert converte_para_romando(3) == 'III'
assert converte_para_romando(4) == 'IV'
assert converte_para_romando(5) == 'V'
assert converte_para_romando(6) == 'VI'
assert converte_para_romando(7) == 'VII'
assert converte_para_romando(8) == 'VIII'
assert converte_para_romando(9) == 'IX'
assert converte_para_romando(10) == 'X'
assert converte_para_romando(16)== 'XVI'
print('Teste OK')