#upondo que a população de um país A seja da ordem de 80000 habitantes
#com uma taxa anual de crescimento de 3% e que a população de B 
#seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
#que calcule e escreva o número de anos necessários para que a população do
#país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a = 80000
pop_b = 200000
anos = 0
cres_a = 0.03
cres_b = 0.015
while (pop_a < pop_b):
    anos += 1
    pop_a = pop_a + (pop_a * cres_a)
    pop_b = pop_b + (pop_b * cres_b)
print("Após {} anos o país A ultrapassou o país B em número de habitantes.".format(anos))
print("País A: {}".format(int(pop_a)))
print("País B: {}".format(int(pop_b)))


