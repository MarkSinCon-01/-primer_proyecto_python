contraseña_correcta = "python123"

for intento in range(3):
    ingreso = input("Ingresa tu contraseña: ")

    if ingreso == contraseña_correcta:
        print("✅ Acceso permitido.")
        break
    else:
        print("❌ Contraseña incorrecta.")

print("Fin del sistema.")