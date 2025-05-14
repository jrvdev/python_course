# Funciones y Condicionales

#funcion basica
def my_function():
    print("Hello word")

#llamada de funcion
my_function()

#funcion con parametros y return
def my_mean(my_list):
    result = sum(my_list) / len(my_list)
    return result
#llamada de la funcion
print(my_mean([1,2,3,4,5]))

#funcion para calcular el area de un cuadrado sabiendo uno de sus lados
def calcule_square_area(longitude):
    return longitude**2
    
print(calcule_square_area(7))

#Convertirdor de onzas liquidas a milimitros
def volumen_converter(fluid_ounces):
    return fluid_ounces * 29.57353
    
print(volumen_converter(5))

#Print vs return en funciones

def example(number):
    print("informacion de la funcion") #se puede utilizar para mostrar informacion
    return number #siempre se recomienda utilizar el return para devolver un valor, ya que si no la funcion devuelve un valor none

print(example(5))


print("================================")
print()

# Condicionales

#If else aplicados, a la funcion mean, para validar si es una lista o un diccionario y hacer el calculo correcto

def my_mean_upgrade(my_value):
    #bloque si es un diccionario
    if(type(my_value) == dict): #el operador == es un operador de comparacion que devuelve true si la comparacion es identica entre ambos operando (valores)
        result = sum(my_value.values()) / len(my_value)
    #bloque si es no es un diccionario osea una lista en este caso
    else:
        result = sum(my_value) / len(my_value)    
    return result

#llamada a la funcion y pasamos los datos
print(my_mean_upgrade([1,2,3,4,5]))
print(my_mean_upgrade({"people1":1, "people2":2, "people3":3, "people4":4, "people5":5}))


#ejemplo simple de condicional donde comparamos si x es identico a 1
x = 1 
 
if x == 1:
    print("Yes")
else:
    print("No")

#Tambien existe los operadores logicos entre ellos estan or(o) y and(y)
"""
donde or devuelve true si uno de la comparacion se cumple, 
mientra que and devuelve true si ambas comparaciones se cumple.
"""

#ejemplo de or y and
def example2(age, gender):
    #el operador >= significa mayor o igual
    if(age >= 18) and (gender == "M" or gender == "F"):
        print(f"Eres mayor de edad y eres {gender}")
    else:
        print(f"Eres menor de edad y eres {gender}")

example2(21, "M")
example2(15, "F")


#Calcular la temperatura 

def warn_or_cold(temperature):
    if(temperature > 7): # > == Mayor
        result = "Warm" #Caliente
    else:
        result = "Cold" #Frio
    return result
    
print(warn_or_cold(10))    
print(warn_or_cold(7)) 
print(warn_or_cold(5))

#Controlador de contraseña

#comprobamos si la longitud de la cadena es menor que 8 (devuelve False) o mayor o igual (True)
def password_controller(password):
     
    if(len(password) < 8):
        return False
    else:
        return True
       
print(password_controller("mypass"))
print(password_controller("mylongpassword"))

#Condicionales con elif
name = "johan"

if(name == "juan"):
    print("Hello 1")
elif(name == "johan"): #al no cumplirse la condicion de if baja al siguiente condicional osea este elif, pueden aver varios elif auque no se recomienda utilizar muchos elif
    print("Hello 2")
else:
    print("Hello 3")