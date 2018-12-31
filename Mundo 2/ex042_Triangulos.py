print("Insira as medidas dos lados dos triângulos")
a = float(input("Lado a:"))
b = float(input("Lado b:"))
c = float(input("Lado c:"))

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c:
        print("TRIÂNGULO EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("TRIÂNGULO ISÓSCELES")
    else:
        print("TRIÂNGULO ESCALENO")
else:
    print("Não formam triângulo.")
