nome = input("Insira seu nome completo: ")
nome.strip()
print(nome.upper())
print(nome.lower())
espacos = nome.count(' ') #conta quantos espaços tem na string
print("O nome completo tem {} letras.".format(len(nome)-espacos))
nomes = nome.split()
print("O primeiro nome tem {} letras.".format(len(nomes[0])))
