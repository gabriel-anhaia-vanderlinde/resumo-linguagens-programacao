import math
ang = float(input('digite o ângulo que você deseja.'))
seno = math.sin(math.radians(ang))
print('seno : {: .2}'.format(seno))
cosseno = math.cos(math.radians(ang))
print('cosseno : {: .2}'.format(cosseno))
tangente = math.tan(math.radians(ang))
print('tangente : {: .2}'.format(tangente))