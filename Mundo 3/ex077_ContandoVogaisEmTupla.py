palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for c in palavras:
    print(f"Na palavra {c.upper()} temos ", end="")
    for i in c:
        if i.lower() in 'aeiou':
            print(f"{i} ", end="")
    print("")