# Variables en python y tipos de datos basicos


# Variables de ejemplos
items = 20
price = 2

total_price = items * price # operacion basica de suma

""" operadores aritmetios en python
+  suma
-  resta
*  multiplicacion
/  division decimal
// divison entera
%  modulo o resto
** exponenciacion
"""

print(items, price, total_price) # impresion de varios elementos

# Tipos de datos basicos
print()
print(type(items)) # la funcion type devuelve la clase del tipo de dato
print(dir(int)) #la funcion dir nos muestra que se puede hacer con esos tipos de datos
print(help(str.upper)) # la funcion help nos muestra la documentacion de cada uno de los metodos de los objetos de las clases de datos.
print()
my_interger = 50 # entero
my_float = 25.5 # decimal
my_string = "Hola" #cadena de caracteres
my_list = [1,25.6,"hello",[2,3,4.5,"hey"]] #lista mixta con otra lista dentro y varios tipos de datos
my_list_range1 = list(range(1, 11)) # una lista con un rango de 1 hasta 10
my_list_range2 = list(range(1, 11, 2)) # lo mismo pero con saltos de 2

print(my_interger, my_float, my_string)
print(my_list_range1, my_list_range2)

# sumar el promedio de una lista

my_notes = [90,60,86.5,80.4,100.0]

my_sum = sum(my_notes) #utilizamos la funcion sum para sumar
my_lenght = len(my_notes)#utilizamos la funcion len para contar el numero de elementos de un contenedor
my_average = my_sum / my_lenght #operacion
print(f"Mi promedio es de: {my_average}") #Esta es otra forma de concatenar utilizando los template string o f string

# para encontrar un valor repetido de una lista utilizamos la funcion count, que nos devuelve el numero de veces que aparece

my_other_list = [1,2,2,2,3,4,5]
print(my_other_list.count(2)) #nos muestra el numero de veces que se repite el valor 2

#para convertir texto en mayuscula o miniscula utilizamos upper() para las mayuscula y lower() para las minusculas

print("hola".upper())
print("HOLA".lower())

#Otro tipo de dato llamado diccionario

# Funciona con un par de clave y valor la clave en este caso es el nombre y el valor en este caso es la edad
my_disccionary_people = {"Juan": 30, "Eduar": 40, "alguien mas": 99} 

print(my_disccionary_people)

# Otro tipo de dato llamado tuplas, son casi iguales que las lista solo que son mas rapidas y no son mutables.

my_tupla1 = (1,2,3,4,5)

print(my_tupla1)

#tupla anidadas
color_code = (("Red", "FF0000"), ("blue", "0000FF"), ("green", "008000"))
print(color_code)

#diccionario con tuplas 
day_temperatures = {
    "morning": (10.3,3.5,4.0), 
    "noon": (20.4,30.5,60.4), 
    "evening": (90.3,40.5,68.0)
}
print(day_temperatures)

#Ver funciones incorporadas
print()

print(dir(__builtins__))

print()