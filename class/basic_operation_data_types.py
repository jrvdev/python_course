# Operaciones basicas con tipos de datos

print('hola'.replace('h','d')) #remplaza la letra h por la d

# operaciones basicas con una lista
numbers = [1,2,3,4,5]

 #Agrega un elemento al final
numbers.append(90)
print(numbers)

#devuelve el indice del elemento dado su valor
print(numbers.index(3)) 

 #Elimina la primera aparicion del elemento
numbers.remove(2)
print(numbers)

#Devolver el elemento dado su indice
print(numbers.__getitem__(4)) 
print(numbers[4]) #Ambos son lo mismo, pero esta es la forma recomendada

#Nos muestra el tamaño de la lista
print(numbers.__len__())
print(len(numbers))#Ambos son lo mismo, pero esta es la forma recomendada

#Devolver una secuencia de la lista donde se incluye el inicio, pero se vuelve uno antes que el ultimo
print(numbers[0:2])
print(numbers[:2]) #es lo mismo
print(numbers[3:5])
print(numbers[3:]) #es lo mismo
print(numbers[-1]) #devuelve el ultimo
print(numbers[-5]) #devuelve el primero
print(numbers[-5:-1]) # tambien funciona con negativos
print("===================")
#Devolver una secuencia de caracteres, funciona igual que una lista

letters = "Hola mundo esto es una cadena"

print(len(letters)) #devuelve la longitud de la cadena

print(letters.index('a')) #devuelve la posicion del primer elemento que coincida
print(letters.count('a')) #devuelve el numero de veces que aparece ese elemento
print(letters[-1]) #devuelve el ultimo elemnto (negativo)
print(letters[28]) #devuelve el ultimo elemnto (positivo)
print(letters[0]) #devuelve el primero (positivo)
print(letters[-29]) #devuelve el primero (negativo)
print(letters[1:8]) 
print(letters[-28:-21]) 
print("===================")
#Llamada de elementos en diccionarios

days = {"monday":1, "friday":2, "saturaday":3}

#Solo funciona llamando a su clave para devolver su valor
print(days["monday"]) #devuelve el primer valor
print(days["saturaday"]) #devuelve el ultimo valor

print("===================")

#Conversion entre tipos de datos
my_tupla = (1,2,3,4,5)
my_lista = [5,4,3,2,1]
my_string = "Hola mundo"
#tupla a lista
print(my_tupla)
my_tupla = list(my_tupla)
print(my_tupla)
print()
#lista a tupla
print(my_lista)
my_lista = tuple(my_lista)
print(my_lista)
print()
#cadena a lista
print(my_string)
my_string_from_list = list(my_string)
print(my_string_from_list)
print()
#lista a cadena


print(my_string_from_list)
my_list_from_string = str.join("",my_string_from_list) #llamamos el metodo str.join para convertirlo a string y que lo separe cada string con un espacio
print(my_list_from_string)