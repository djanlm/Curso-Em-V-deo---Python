def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


name = str(input("Nome do jogador: ")).strip()
goals = str(input("Número de gols: "))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

if name == "" and goals == 0:
    ficha()
elif name == "":
    ficha(gols=goals)
elif goals == 0:
    ficha(name)
else:
    ficha(name, goals)