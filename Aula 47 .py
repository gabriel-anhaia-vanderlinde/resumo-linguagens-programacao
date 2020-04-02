    
populacoes = True
while populacoes: 
    pop_a = int(input('informe a população da cidade A: '))
    pop_b = int(input('informe a população da cidade B: '))
    anos = 0
    cres_a = float(input('informe a taxa de crescimento da população da cidade A: '))
    cres_b = float(input('informe a taxa de crescimento da população da cidade B: '))
    while (pop_a < pop_b):
        anos += 1
        pop_a = pop_a + (pop_a * cres_a)
        pop_b = pop_b + (pop_b * cres_b)
        if pop_a > pop_b:
            print("Após {} ano(s) o país A ultrapassara o país B em número de habitantes.".format(anos))
            print("País A: {}".format(int(pop_a)))
            print("País B: {}".format(int(pop_b)))
        else:
            print('Após {} ano(s) a cidade A ainda não atingiu ou superou a quantidade de habitantes da cidade B'.format(anos))
    escolha = input('Quer fazer uma contagem relacionando as populações? S/N :')
    if escolha == 'N' or escolha == 'n':
        break
