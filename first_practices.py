#Primera practica para reforzar los fundamentos.

"""
Crear un programa que le pida al usuario en que piensas, repitadas veces y luego que al utilizar '/end' termine de preguntar
y muestre las cosas que escribio con la primera letra en mayusculas de cada palabra.

la salida debe ser limpia sin llaves o corchetes solo el texto.

"""

#input de pregunta
def say_somenthing():
   somenthing = input("¿Say somenthing? ")
   return somenthing

#convertimos a string la lista y imprimimos las palabras cada una al iniciar en mayuscula
def string_to_pharase(pharaseToString):
    pharaseToString = str.join(" ",pharaseToString).capitalize()
    return pharaseToString

#lista para las frases
pharase = []

#ejecucion del programa
while True:
    value = say_somenthing()
    #evaluamos las operaciones
    if(value == "/end"):
        break
    else:
        pharase.append(value)
        continue

print(string_to_pharase(pharase))
