# Lectura y Escritura basica de archivos de texto con python

#Lecturas

#lee el archivo completo
with open("fille.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# .read(): lee todo el contenido como un string.
print()

#lee el archivo linea por linea
with open("fille.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip()) 
        
# .strip() elimina los saltos de línea \n al final de cada línea.
print()

# Guardar líneas en una lista
with open("fille.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)
# .readlines() devuelve una lista, donde cada elemento es una línea.

#  Manejar errores con try-except
try:
    with open("fille.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("❌ Archivo no encontrado.")

print()
#Escrituras

#Esto crea un archivo de texto (modifica(borra el anterior y remplaza con el nuevo))
with open("saludo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo creado con Python.\n")
    archivo.write("¡Funciona!\n")

#Esto permite agregar mas datos al archivo
with open("saludo.txt", "a") as archivo:
    archivo.write("Otra línea añadida sin borrar lo anterior.\n")
