pos1 = None
pos2 = None
pos3 = None
pos4 = None
pos5 = None
pos6 = None
pos7 = None
pos8 = None
pos9 = None
opcao_tabuleiro = 0
print('''
Para jogar digite o numero correspondete ao que voçê quer fazer sua jogada.
    {0} | {1} | {2}
    ---------------
    {3} | {4} | {5} 
    ---------------
    {6} | {7} | {8}   
'''.format(pos1 or 1,pos2 or 2,pos3 or 3,pos4 or 4,pos5 or 5, \
    pos6 or 6,pos7 or 7,pos8 or 8,pos9 or 9))

turno_incorreto = True
jogador = None

while turno_incorreto:
    opcao = input('Quer começar com x ou o : ')
    
    if opcao == 'x' or opcao == 'X':
        turno_incorreto = False
        jogador = 'X'
    elif opcao == 'o' or opcao == 'O':
        turno_incorreto = False
        jogador = 'O'
    else:
        print('Opcâo invalida')

jogo_acabou = False

while not jogo_acabou:
    print('''
    o jogador que vai jogar é {9}
    {0} | {1} | {2}
    ---------------
    {3} | {4} | {5} 
    ---------------
    {6} | {7} | {8}   
'''.format(pos1 or 1,pos2 or 2,pos3 or 3,pos4 or 4,pos5 or 5, \
    pos6 or 6,pos7 or 7,pos8 or 8,pos9 or 9, jogador))

    opcao_incorreta = True
    posicao_ocupada = True
    opcao_tabuleiro = None
    while opcao_incorreta or posicao_ocupada:
        opcao_tabuleiro = input('Informe a posição desejada')
        if opcao_tabuleiro.isnumeric():
            opcao_tabuleiro =int(opcao_tabuleiro)
        else:
            print('A opção {} não é valida'.format(opcao_tabuleiro))
        if opcao_tabuleiro == 1 or opcao_tabuleiro == 2 or opcao_tabuleiro == 3 or opcao_tabuleiro == 4 or opcao_tabuleiro == 5 or opcao_tabuleiro == 6 or opcao_tabuleiro == 7 or opcao_tabuleiro == 8 or opcao_tabuleiro == 9:
            opcao_incorreta = False
        else:
            print('Informe uma opcao valida')
     
        if opcao_tabuleiro == 1:
            if pos1 == None:
                pos1 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 2:
            if pos2 == None:
                pos2 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 3:
            if pos3 == None:
                pos3 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 4:
            if pos4 == None:
                pos4 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 5:
            if pos5 == None:
                pos5 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 6:
            if pos6 == None:
                pos6 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 7:
            if pos7 == None:
                pos7 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 8:
            if pos8 == None:
                pos8 = jogador
                posicao_ocupada = False
            else:
                print('posição ocupada')
        elif opcao_tabuleiro == 9:
            if pos9 == None:
                pos9 = jogador
                posicao_ocupada = False
            
    if pos1 != None and pos1 == pos2 and pos1 == pos3:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos1))
    elif pos1 != None and pos1 == pos4 and pos1 == pos7:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos1))
    elif pos1 != None and pos1 == pos5 and pos1 == pos9:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos1))
    elif pos4 != None and pos4 == pos5 and pos4 == pos6:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos4))
    elif pos7 != None and pos7 == pos8 and pos7 == pos9:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos7))
    elif pos3 != None and pos3 == pos5 and pos3 == pos7:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos3))
    elif pos2 != None and pos2 == pos5 and pos2 == pos8:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos2))
    elif pos3 != None and pos3 == pos6 and pos3 == pos9:
        jogo_acabou = True
        print('Quem Ganhou foi {}'.format(pos3))
    elif pos1 != None and pos2 != None and pos3 != None and  pos4 != None and  pos5 != None and pos6 != None and  pos7 != None and  pos8 != None and  pos9 != None:
        print('Empate, comece novamente')
        jogo_acabou = True
            

    
    if jogador == 'X':
        jogador = 'O'
    elif jogador == 'O':
        jogador = 'X'

jogo_acabou = True