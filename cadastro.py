from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome:'))
nasc = int( input('Ano de nasimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho(0 não tem):'))
print(dados)