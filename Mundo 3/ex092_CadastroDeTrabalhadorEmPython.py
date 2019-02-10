import datetime
now = datetime.datetime.now()
anoAtual = now.year
dic = dict()
dic['nome'] = str(input("Nome: "))
dic['nascimento'] = int(input("Ano de nascimento: "))
idade = anoAtual - dic['nascimento']
dic['idade'] = idade
dic['carteira'] = int(input("Carteira de Trabalho (0, não tem): "))
if dic['carteira'] != 0:
    dic['contratacao'] = int(input("Ano de contratação: "))
    dic['salario'] = float(input("Salário: R$ "))
    idadeContratacao = dic['contratacao']-dic['nascimento']
    dic['aposentadoria'] = idadeContratacao + 35  #considerando que demora 35 anos pra se aposentar desde a contratacao
print("-="*30)
print(dic)
for k, v in dic.items():
    print(f'{k}: {v}')