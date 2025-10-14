# 1. Guardamos el número secreto
numero_secreto = 7

# 2. Pedimos el primer intento del usuario
intento = int(input("Adivina el número secreto (entre 1 y 10): "))

# 3. Mientras el intento no sea igual al número secreto
while intento != numero_secreto:
    print("❌ Ese no es el número. Intenta de nuevo.")
    
    # 4. Volvemos a pedir un nuevo intento
    intento = int(input("Adivina otra vez: "))

# 5. Cuando el usuario acierta, sale del bucle y muestra este mensaje
print("✅ ¡Correcto! Has adivinado el número secreto.")