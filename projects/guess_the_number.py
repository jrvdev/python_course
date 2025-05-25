import random

def game():
    number_secret = random.randint(1, 100)
    attempts = 0

    print("🎯 Adivina el número (entre 1 y 100)")

    while (True):
        attempt = int(input("Tu inteno: "))
        attempts += 1

        if(attempt < number_secret):
            print("🔼 Más alto")
        elif(attempt > number_secret):
            print("🔽 Más bajo")
        else:
            print(f"🎉 ¡Correcto! El número era {number_secret} . Intentos : {attempts}")
            break


def play_again():
    while (True):
        game()
        again = input("¿Quieres jugar otra vez? (sí/no): ").strip().lower()
        if (again != "si"):
            print("¡Gracias por jugar! 👋")
            break

play_again()


"""
✅ Extensiones si quieres subir el nivel:
🕵️‍♂️ Límite de intentos (ej: máximo 7)

📈 Guardar récord de la mejor puntuación

🧠 Modo difícil: números del 1 al 1000

🧪 Validar que el usuario ingrese un número

"""