frase = str(input("Digite uma frase para saber se ela é palíndromo: ")).strip().replace(" ", "") #o replace remove os espaços

frase2 = ""
#inverte a frase
for i in frase:
    frase2 = i + frase2

if frase == frase2:
    print("A frase é palíndromo.")
else:
    print("A frase não é palíndromo.")

#frase2 = frase[::-1] --> Outra forma de inverter.