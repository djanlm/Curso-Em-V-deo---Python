def leiaInt(string):
    while True:
        num = str(input(string)).strip()
        if num.isnumeric():
            num = int(num)
            break
        else:
            print("\033[0;31mERRO! Digite um número inteiro.\033[m")
    return num


# main program
n = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {n}')