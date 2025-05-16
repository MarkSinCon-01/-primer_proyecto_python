# registrar_notas.py

print("📚 Registro de notas escolares")

while True:
    nombre = input("Nombre del estudiante: ")
    materia = input("Materia: ")
    nota = input("Nota: ")

    # Guardamos en el archivo
    with open("notas.txt", "a") as archivo:
        archivo.write(f"{nombre},{materia},{nota}\n")

    otro = input("¿Deseas agregar otro estudiante? (s/n): ")
    if otro.lower() != "s":
        break

print("✅ Notas registradas correctamente.")