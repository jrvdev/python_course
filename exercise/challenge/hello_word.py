""""
✅ Desafío Final de la Clase
Crea un programa que:

Pida tu nombre y edad.

Si eres mayor de edad, te diga "Bienvenido adulto", si no, "Hola joven".

Te dé la opción de repetir (usando un ciclo while) hasta que escribas "salir".
"""

def welcome(age):
    if(age >= 18):
        return "Bienvenido adulto"
    else:
        return "Hola joven"



while(True):
    name = input("ingresa tu nombre: ")
    age = int(input("ingrese su edad: "))

    message = welcome(age)
    print(f"{message}, {name}")

    exit = input("Escribe 'salir' para terminar el programa: ").strip().lower()
    if(exit == "salir"):
        break

def clasificar(numero):
    if (numero > 0):
        return "positivo"
    elif (numero < 0):
        return "negativo"
    else:
        return "cero"
    