
from datetime import datetime

funcionario = {}

funcionario['nome'] = input('Informe o nome do funcionário ')
funcionario['ano_nasc'] = int(input('Informe o ano de nascimento do funcionário: '))
funcionario['idade'] = datetime.now().year - funcionario.get('ano_nasc')
funcionario['ctps'] = input('Informe a CTPS do fincionário, ou 0 caso não tenha: ')
if (funcionario.get('ctps') != '0'):
    funcionario['ano_cont'] = int(input('Informe o ano de contratação:'))
    funcionario['salario'] = float(input('Informe o salário do funcionário: R$ '))

funcionario['ano_apon'] = funcionario.get('ano_cont') + 30

print(f'Nome: {funcionario.get("nome")}')
print(f'Idade: {funcionario.get("idade")}')
print(f'Ano aposentadoria: {funcionario.get("ano_apon")}')
