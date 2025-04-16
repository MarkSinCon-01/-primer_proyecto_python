import random

def adivina_el_número(x):
    print("==============================")
    print(" 🎮 ¡Bienvenido al Juego! 🎮 ")
    print("==============================")
    print(f"Tu meta es adivinar el número generado por la computadora entre 1 y {x}.")

    numero_aleatorio = random.randint(1, x)  # Genera un número aleatorio entre 1 y x
    prediccion = None  # Inicializamos la variable en None
    intentos = 0  # Contador de intentos

    while prediccion != numero_aleatorio:
        try:
            prediccion = int(input(f"\nAdivina un número entre 1 y {x}: "))  # Entrada del usuario
            intentos += 1  # Aumentamos el contador de intentos

            if prediccion < 1 or prediccion > x:
                print(f"⚠️ El número debe estar entre 1 y {x}. Intenta de nuevo.")
            elif prediccion < numero_aleatorio:
                print("🔼 Intenta otra vez. Tu número es muy pequeño.")
            elif prediccion > numero_aleatorio:
                print("🔽 Intenta otra vez. Tu número es muy grande.")

        except ValueError:
            print("⚠️ Entrada inválida. Por favor, ingresa un número.")

    print(f"\n🎉 ¡Felicidades! Adivinaste el número {numero_aleatorio} correctamente en {intentos} intentos. 🎉")

# Llamamos a la función con un rango de 1 a 10
adivina_el_número(10)