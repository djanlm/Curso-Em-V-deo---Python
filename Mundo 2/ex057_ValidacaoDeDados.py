sexo = str(input("Insira o sexo (M/F): ")).upper().strip()

while sexo != 'M' and sexo != 'F':
    print("\033[33mDados inseridos são inválidos.\033[m")
    sexo = str(input("Insira o sexo (M/F) ")).upper().strip()