usuario_senha_invalidos = True

while usuario_senha_invalidos:
    usuario = input('Informe um nome de usuario')
    senha = input('informe uma senha diferente ')
    if usuario == senha:
        print('Informe uma senha ou usuario diferente: ')
    else:
        print('Seu usuario e senha foram cadastrados, bem vindo {} '.format(usuario))
        usuario_senha_invalidos = False