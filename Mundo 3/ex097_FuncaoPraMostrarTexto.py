def escreva(txt):
    tam = len(txt)
    tam += 4
    print("~" * tam)
    print(f"{txt:^{tam}}")
    print("~" * tam)


# Main Program
escreva("Olá, Mundo!")
