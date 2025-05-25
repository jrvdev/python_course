import random
import os

# Archivo donde se guarda el mejor puntaje
BEST_SCORE_FILE = "projects/best_score.txt"

# Cargar el mejor puntaje desde el archivo, si existe
def load_best_score():
    if os.path.exists(BEST_SCORE_FILE):
        with open(BEST_SCORE_FILE, "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return None
    return None

# Guardar el nuevo mejor puntaje en el archivo
def save_best_score(score):
    with open(BEST_SCORE_FILE, "w") as file:
        file.write(str(score))

# Validar si el número ingresado está entre 1 y 100
def is_valid_number(n):
    return 1 <= n <= 100

# Comparar el intento del usuario con el número secreto
def check_guess(guess, secret_number):
    if guess < secret_number:
        print("🔼 ¡Más alto!")
        return False
    elif guess > secret_number:
        print("🔽 ¡Más bajo!")
        return False
    else:
        print("🎉 ¡Correcto!")
        return True

# Ejecutar una sola partida del juego
def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    MAX_ATTEMPTS = 10
    best_score = load_best_score()

    print("\n🎯 Adivina el número (entre 1 y 100)")
    print(f"📉 Tienes un máximo de {MAX_ATTEMPTS} intentos.")

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input("Tu intento: "))
            if not is_valid_number(guess):
                print("⚠️ El número debe estar entre 1 y 100.")
                continue
        except ValueError:
            print("⚠️ Entrada no válida. Por favor, ingresa un número.")
            continue

        attempts += 1
        if check_guess(guess, secret_number):
            print(f"🥳 ¡Adivinaste en {attempts} intento(s)!")
            # Verificar si es el mejor puntaje
            if best_score is None or attempts < best_score:
                print("🏆 ¡Nuevo récord personal!")
                save_best_score(attempts)
            else:
                print(f"📊 Tu mejor puntaje es {best_score} intento(s).")
            return

    print(f"💥 ¡Se acabaron los intentos! El número era {secret_number}.")
    if best_score:
        print(f"📊 Tu mejor puntaje sigue siendo {best_score} intento(s).")

# Bucle principal para jugar varias veces
def game_loop():
    while True:
        play_game()
        again = input("\n¿Quieres jugar otra vez? (sí/no): ").strip().lower()
        if again != "si":
            print("👋 ¡Gracias por jugar!")
            break

# Iniciar el programa
game_loop()
