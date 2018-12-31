from datetime import date

ano = int(input("Digite um ano para saber se ele é bissexto: "))
if ano == 0:
    ano = date.today().year #se o usuario digitar 0, o programa usa o ano atual
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("Esse ano é bissexto")
        else:
            print("Esse ano não é bissexto")
    else:
        print("Esse ano é bissexto")
else:
    print("Esse não ano é bissexto")