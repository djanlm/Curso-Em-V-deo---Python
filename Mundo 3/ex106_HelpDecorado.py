def escreva(txt):
    tam = len(txt)
    tam += 4
    print("~" * tam)
    print(f"{txt:^{tam}}")
    print("~" * tam)


def pyHelp(msg):
    print("\033[1;37;40m", end="")
    help(msg)
    print("\033[m", end="")

while True:
    print("\033[1;30;42m", end="")
    escreva("SISTEMA DE AJUDA PyHELP")
    print("\033[m", end="")
    comando = str(input("Função ou Biblioteca > ")).strip()
    if comando in "fimFIM":
        print("\033[1;30;41m", end="")
        escreva("Até Logo!!")
        print("\033[m", end="")
        break
    print("\033[1;30;44m", end="")
    escreva(f"Acessando o manual do comando {comando}")
    print("\033[m", end="")
    pyHelp(comando)

