lista = list()
dic = dict()
somaIdade = 0
user = ""
while True:
    dic['nome'] = str(input("Nome: ")).strip()
    while True:
        dic['sexo'] = str(input("Sexo: [M/F] ")).strip().upper()
        if dic['sexo'] in 'MF':
            break
        else:
            print("Erro!! Por favor, digite apenas M ou F.")
    dic['idade'] = int(input("Idade: "))
    somaIdade += dic['idade']
    lista.append(dic.copy())
    while True:
        user = str(input("Quer continuar? [S/N] ")).strip().upper()
        if user in 'SN':
            break
        else:
            print("Erro!! Por favor, digite apenas S ou N.")
    if user in "N":
        break
media = somaIdade/len(lista)
print("-="*25)
print(f"- O grupo tem {len(lista)} pessoas.")
print(f"- A média de idade é de {media:.2f} anos.")
print(f"- As mulheres cadastradas foram: ",end='')
for c in lista:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=" ")
print(f"\n- Lista das pessoas que estão acima da média: ")
for c in lista:
    for k, v in c.items():
        if c['idade'] > media:
            print(f"{k} = {v}", end="; ")
    print("")
print("<< ENCERRADO >>")