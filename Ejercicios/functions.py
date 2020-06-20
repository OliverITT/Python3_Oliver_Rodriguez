def tiponumero (numero):
    if numero > 0:
            print("numero es positivo")
    elif numero == 0:
            print("Numero es cero")
    elif numero < 0:
            print("Numero es negativo")

def paroimpar (num):
    if num % 2 == 0:
        print("numero es par")
    else:
        print("numero es impar")

def primo (numero):
    divcont = 0
    div = 0
    while (divcont < 3 and div <= numero):
        div += 1
        if numero % div == 0:
            divcont += 1
    if divcont == 2:
        print("numero es primo")
    else:
        print("numero no es primo")

def aniobisiesto (anio):
    if anio % 4 == 0 or anio % 400 == 0 or anio % 100 == 0:
        print("anio bisiesto")
    else:
        print("anio no es bisiesto")