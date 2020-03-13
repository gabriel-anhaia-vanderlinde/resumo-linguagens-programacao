reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda da reta: '))
reta3 = float(input('Informe o valor da terceira da reta: '))
if reta1 == reta2 and reta2 == reta3:
    print('É Equilatero')
elif reta1 == reta2 and reta2 != reta3:
    print('É isosceles')
elif reta1 != reta2 and reta2 == reta3:
    print('É isosceles')
elif reta1 == reta3 and reta2 != reta1:
    print('É isosceles')
else:
    print('É Escaleno')