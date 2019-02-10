countp = 0
exp = str(input("Digite uma expressão usando apenas parênteses: ")).strip()
for c in exp:
    if c == '(':
        countp += 1
    elif c == ')':
        countp -= 1

if countp == 0:
    print("A expressão digitada é válida.")
else:
    print("A expressão digitada não é válida.")