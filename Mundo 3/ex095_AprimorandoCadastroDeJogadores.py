dic = {}
lista = []  # List to store the dictionary of soccer players
while True:
    dic['nome'] = str(input("Nome do jogador: "))
    partidas = int(input("Quantas partidas ele jogou?"))
    dic['gols'] = []
    for c in range(0, partidas):
        dic['gols'].append(int(input(f"Quantos gols na partida {c}? ")))
    total = sum(dic['gols'])
    dic['total'] = total
    lista.append(dic.copy())
    user = str(input("Quer continuar? [S/N]")).upper().strip()
    if user == "N":
        break
    print("-"*25)
print("-="*30)
print(f"{'cod':<4}{'nome':<15}{'gols':<15}{'total'}")
print("-"*40)

for i, c in enumerate(lista):
    print(f"{i:>3} {c['nome']:<15}{str(c['gols']):<15}{c['total']}")  # I had to convert c['goals'] into string to use :
print("-"*40)

while True:
    jogador = int(input("Mostrar dados de qual jogador: [999 para sair]"))
    if jogador == 999:
        break
    if jogador < len(lista):
        print(F"---FLEVANTAMENTO DO JOGADOR {lista[jogador]['nome']} ---")
        for i, c in enumerate(lista[jogador]['gols']):
            print(f"No jogo {i+1} fez {c} gols.")
    else:
        print(f"ERRO!! Não existe jogador com código {jogador}")

print("<<< VOLTE SEMPRE >>>")