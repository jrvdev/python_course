#Bucles o ciclos en python

#Bucles for
letters = "Hola mundo"
numbers = [1,2,3,4,5,6,7,8,9,10]

#imprime cada elemento de la lista o cadena
for letter in letters:
    print(letter)

print() #espacio

for number in numbers:
    print(number)

print("==== \n")
#imprime cada elemento del diccionario (keys, values) o items (ambos)

peoples = {"Johan": 21, "johns": 93, "algo": 40}

for person in peoples.items(): #Ambos
    print(person)

for person in peoples.keys(): #llaves
    print(person)

for person in peoples.values(): #valores
    print(person)


#Esto recorre cada elemento del diccionario y lo imprime
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

#almacena los valores de llave y valor del diccionario, es importante ponerlos en orden, el nombre de las variables no importa, pero es mejor tenerlo claro y simple para mejor legibilidad
for key, value in phone_numbers.items():
    print(f"{key}: {value}")

print()
#reemplazamos una cadena por otra utilizando el metodo replace(vieja cadena, nueva cadena)
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for phone in phone_numbers.values():
    numbers = phone.replace("+","00")
    print(numbers)

#Bucle while

#En este bucle continua siempre que la condicion sea verdadera

#continue, es para continuar y break es para terminar.

#siempre inicia el bucle
while True:
    username = input('Cual es tu nombre: ')
    if(username != "johan"): #si el nombre no es johan vuelve a ejecutar
        continue
    else: #si el nombre es johan termina la ejecucion
        break