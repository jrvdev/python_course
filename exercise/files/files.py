"""
1) Crea un archivo llamado datos.txt con nombres o frases.

2)Crea un script que:

Lea cada línea

Imprima la línea en mayúsculas

Numere cada línea

Ignore las líneas vacías

"""

import os

#Lectura de archivos
def read_file():
    number_line = 0
    try:
        with open("exercise/data.txt", "r") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:  # Ignorar líneas vacías
                    number_line += 1
                    print(f"{number_line}. {clean_line.upper()}")
    except FileNotFoundError:
        print("❌ Archivo no encontrado.")


#Escritura de archivos
def write_file():
    name = input("📄 Escribe el nombre del archivo a crear (ej: notas.txt): ").strip()
    # Evalúa si contiene la extensión
    if not name.endswith(".txt"):
        name += ".txt"

    # Ruta donde se almacena el archivo
    os.makedirs("exercise", exist_ok=True)  # crea el directorio si no existe
    route = f"exercise/{name}"
    
    # Verifica si el archivo ya existe
    if os.path.exists(route):
        answer = input("⚠️ El archivo ya existe. ¿Deseas sobrescribirlo? (s/n): ").strip().lower()
        if answer != "s":
            print("❌ Operación cancelada.")
            return
    else:
        # Si no existe, definimos answer para evitar error
        answer = "s"

    print("📝 Escribe tus frases. Escribe 'salir' para terminar.")
    
    # Escritura del archivo
    with open(route, "w") as file:
        while True:
            # Captura de las frases
            line = input("➡️ Frase: ").strip()
            # Salida de la escritura
            if line.lower() == "salir":
                print(f"✅ Archivo '{name}' guardado correctamente en {route}.")
                break
            # Escritura con salto de línea
            file.write(line + "\n")


#Lectura y escritura de archivos
def process_file(input_path, output_path):
    number_line = 0
    try:
        with open(input_path, "r") as file_in, open(output_path, "w") as file_out:
            for line in file_in:
                clean_line = line.strip()
                if clean_line: # devuelve las lineas limpias
                    number_line += 1
                    line_final = f"{number_line}. {clean_line.upper()}\n"
                    file_out.write(line_final)
        print(f"✅ Archivo procesado correctamente. Guardado en '{output_path}'")
    except FileNotFoundError:
        print("❌ El archivo de entrada no fue encontrado.")


#definir ruta de salida
name_file = input("dale un nombre al archivo: ")

#Ejecutar las funciónes
read_file()
write_file()
process_file("exercise/data.txt", f"exercise/{name_file}")



