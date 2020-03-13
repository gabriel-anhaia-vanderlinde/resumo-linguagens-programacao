valor = float(input('Digite o valor do produto'))
forma_de_p = int(input('''
DIgite 1 para pagamento a vista com cartão ou boleto, 
Digite 2 para pagar a vista com cartão,
Digite 3 para pagamento em duas vezes no cartão,
Digite 4 para pagamento em treê vezes ou mais no cartão:  
'''))
pag_vdc = valor - (valor * 0.10)
pag_cc = valor - (valor * 0.05)
pag_dv = valor
pag_3vm = valor + (valor * 0.2)

if forma_de_p == 1:
    print('O valor pago sera de {}'.format(pag_vdc))
elif forma_de_p == 2:
    print('O valor pago sera de {}'.format(pag_cc))
elif forma_de_p == 3:
    print('O valor pago sera de {}'.format(pag_dv))
elif forma_de_p == 4:
    print('O valor pago sera de {}'.format(pag_3vm))
else:
    print('Algo está errado')      