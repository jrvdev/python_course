#Compresion de lista, no es mas que la forma corta de manejar listas

#suponiendo que son temperaturas reales nos llegan de un servidor convertido en enteros (para ahorrar espacio en disco)
temps = [903,495,599,339]

#forma corta de iterar cada elemento con un bucle for en una lista
def simple_list_comprehension():
    new_temps = [temp / 10 for temp in temps]
    return new_temps

print(simple_list_comprehension())

#su equivalente sin utilizar la comprension de lista seria
def equivalent_list_basic():
    new_temps = []
    for temp in temps:
        new_temps.append(temp / 10)
    return new_temps

print(equivalent_list_basic())

print()
#En este caso los valores de las temperaturas pueden contener valores corruptos por ejemplo negativos, como utilizamos condicionales (if else)

other_temps = [903, 495, 599, -9999, 230]
#cuando utilizamos if else la impresion va primero, seguido de la condicon y por ultimo las iteraciones
#pero si solo utilizamos if, la condicion cambiara la posicion con las iteraciones
#new_temps = [temp / 10 for temp in temps if temp != -999]
def condional_list_comprehension():
    new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
    return new_temps

print(condional_list_comprehension())

#su equivalente sin utilizar la comprension de lista seria
def equivalent_list_condicional():
    new_temps = []
    for temp in temps:
        if(temp != -999):
            new_temps.append(temp / 10)
        else:
            new_temps.append(0)
    return new_temps

print(equivalent_list_condicional())

print()
#otro caso seria hacer un filtro de enteros y cadenas
my_list = [99, 'no data', 95, 94, 'no data']

def filter_list_comprehension(list):
    return [number for number in list if  isinstance(number, int)]
print(filter_list_comprehension(my_list))

#su equivalente sin utilizar la comprension seria

#evaluar si es entero
def is_integer(valor):
    return isinstance(valor, int)

def equivalent_filter_list():
    my_new_list = list(filter(is_integer, my_list))
    return my_new_list

print(equivalent_filter_list())



