#Mas sobre funciones

#funciones con multiples parametros

#Esta es un ejemplo basico
def two_string(first, second):
    return first + " " + second
    
print(two_string("hola", "mundo"))


#funciones con argumentos por defecto y orden diferente de parametros

'''
Siempre que el argumento por defecto se agrega de primero,
los demas tambien deben tenerlo,
pero si solo es el ultimo no hay problema de sintaxis
'''
def defaut_parameters(first = "10", second = "Hola"):
    return first + " " + second

#tambien podemos llamar los parametros en diferente orden, pero solo se mostrara el calculo segun los argumentos de ordenados en la funcion
print(defaut_parameters(second="Adios", first= "Mundo")) 


#funciones con argumentos arbitrarios, no se pueden manipular los parametros

#utilizamos el * seguido del nombre del argumento, por convencion se utiliza args
def arguments_arbitrary(*args): #devuelve una tupla
    return args 

print(type(arguments_arbitrary("hola",2,4,4,"mundo",True,float))) 

print(arguments_arbitrary("hola",2,4,4,"mundo",True,float))

#Funciones con un número arbitrario de argumentos de palabra clave
#utilizamos 2 asteriscos(*) y el nombre por convencion es kwargs
#esta coleccion sera un diccionario
def arguments_arbitrary2(**kwargs):
    return kwargs
print(type(arguments_arbitrary2(a = 1, b = 2, c = 3)))
print(arguments_arbitrary2(a = 1, b = 2, c = 3))