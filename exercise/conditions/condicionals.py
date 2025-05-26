"""Ejercicio:
Pide al usuario su edad con input() y dile si puede votar (mayor o igual a 18).
"""

user_age = int(input("Ingresa tu edad: "))

def user_vote(age):
    if (age >= 18):
       return "Puedes votar"
    else:
       return "No puedes votar"

print(user_vote(user_age))