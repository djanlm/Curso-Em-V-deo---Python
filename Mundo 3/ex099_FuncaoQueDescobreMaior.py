def maior(* n):
    print("-="*20)
    print("Analisando os valores passados...")

    maior = n[0]
    if len(n) > 1:
        print(f"Foram informados {len(n)} valores ao todo: ", end="")
        for c in n:
            print(f"{c} ", end="")
            if maior < c:
                maior = c
    else:
        print(f"{len(n)} valor foi informado: {n[0]}", end="")
    print(f"\nO maior número é {maior}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
