import random  # Importamos la biblioteca random para generar números aleatorios

# 1. Generamos un número secreto aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# 2. Definimos la cantidad de intentos que el usuario tiene
intentos_maximos = 3
intentos_realizados = 0  # Esta variable llevará el conteo

# 3. Comenzamos el bucle 'while'
while intentos_realizados < intentos_maximos:
    intento = int(input("Adivina el número secreto (entre 1 y 10): "))
    intentos_realizados += 1  # Sumamos 1 intento

    if intento == numero_secreto:
        print("✅ ¡Correcto! Has adivinado el número secreto.")
        break  # Salimos del bucle si adivina
    else:
        # Pista: ¿es mayor o menor?
        if intento < numero_secreto:
            print("🔼 El número secreto es mayor.")
        else:
            print("🔽 El número secreto es menor.")

        # Mostrar cuántos intentos quedan
        intentos_restantes = intentos_maximos - intentos_realizados
        if intentos_restantes > 0:
            print(f"❌ Intento incorrecto. Te quedan {intentos_restantes} intento(s).\n")
        else:
            print("🚫 Has agotado todos tus intentos.\n")

# 4. Mostrar el número correcto si el usuario no adivinó
if intento != numero_secreto:
    print(f"📢 El número secreto era: {numero_secreto}")
    
#------Proceso Adivinar_Numero_Secreto

    Definir numero_secreto, intento Como Entero

    numero_secreto <- 7

    Escribir "Adivina el número secreto (entre 1 y 10):"
    Leer intento

    Mientras intento <> numero_secreto Hacer
        Escribir "❌ Ese no es el número. Intenta de nuevo."
        Escribir "Adivina otra vez:"
        Leer intento
    FinMientras

    Escribir "✅ ¡Correcto! Has adivinado el número secreto."

FinProceso-------#