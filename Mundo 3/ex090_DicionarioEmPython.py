dic = {}
dic['nome'] = str(input("Nome: "))
dic['media'] = float(input(f"Média de {dic['nome']}: "))
if dic['media'] >= 7:
    dic['situacao'] = 'Aprovado'
elif dic['media'] < 5:
    dic['situacao'] = 'Reprovado'
else:
    dic['situacao'] = 'Recuperação'

    # da pra fazer um for aqui tb.
print(f'Nome é igual a {dic["nome"]}')
print(f'Média é igual a {dic["media"]}')
print(f'Situação é igual a {dic["situacao"]}')

