# Entrada basica del usuario
# con la funcion input podemos pedir un valor al usuario por el teclado

def warn_or_cold(temperature):
    if(temperature > 7): # > == Mayor
        result = "Warm" #Caliente
    else:
        result = "Cold" #Frio
    return result

#Utilizamos la funcion pero convertimos el resultado a un int (entero), ya que input devuelve string.

user_input = int(input('Ingrese la temperatura: '))

print(warn_or_cold(user_input))


#Formateo de cadenas en python
# para las versiones de python 2 0 3 ( utilizamos el %s) donde %s es donde estara la variable
# y para las versiones de 3.6 en adelante utilizamos el f template (f"") donde el {} es donde estara las variables

name_user = input("Cual es tu nombre: ")
surname_user = input("Cual es tu apellido: ")
menssage = "Hola %s %s" % (name_user, surname_user) #utilizamos parentesis cuando hay mas de 1 variable
print(menssage)
menssage = f"Hola {name_user} {surname_user}"
print(menssage)

#Utilizar la version segun el caso personal o necesario

#Otra forma de formatear cadenas es utilizando la funcion .format , donde cada {} es donde va una variable

name = "Dark"
surname = "Black"
 
message = "Your name is {}. Your surname is {}".format(name, surname) 
print(message)