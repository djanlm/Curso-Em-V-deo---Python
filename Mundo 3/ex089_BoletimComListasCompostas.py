notas = []
estudante = []
turma = []
while True:
    nome = str(input("Nome: ")).strip()
    for i in range(0, 2):
        notas.append(float(input(f"Nota {i+1}: ")))
    user = str(input("Quer continuar? [s/n] "))
    estudante.append(nome)
    estudante.append(notas[:])
    turma.append(estudante[:])
    notas.clear()
    estudante.clear()
    if user in 'nN':
        break

print("-="*30)
print("No. NOME"+" "*10+"MÉDIA")
print("-"*25)
for c in range(0, len(turma)):
    print(f"{c:02d}  {turma[c][0]:<15} {(turma[c][1][0]+turma[c][1][1])/2:>4.1f}")

while True:
    print("-" * 25)
    aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if aluno == 999:
        break
    if aluno < len(turma):  #esse if evita que ocorra erro por acesso a posicao invalida na lista
        print(f"Notas de {turma[aluno][0]} são {turma[aluno][1]}")
