from random import randint
print("=-"*15)
print("Vamos jogar par ou ímpar")
print("=-"*15)
c = 0
o = ''
while True:
    pc = randint(0, 10)
    n = int(input("Diga um valor: "))

    while o != 'P' and o != 'I':
        o = str(input("Par ou Ímpar? [P/I]: ")).upper().strip()

    tot = pc + n
    if tot % 2 == 0:
        jogo = "P"
        resultado = 'PAR'
    else:
        jogo = "I"
        resultado = 'ÍMPAR'
    print("-"*20)
    print(f'Você jogou {n} e o computador jogou {pc}. Total de {tot} deu {resultado}')
    print("-" * 20)
    if o != jogo:
        break
    else:
        print("Você VENCEU!!")
    c = c + 1
    o = ''
print(f"Você perdeu depois de ganhar {c} vez(es).")