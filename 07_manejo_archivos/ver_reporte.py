# ver_reporte.py

print("📄 Reporte de Notas")
print("====================")

try:
    with open("notas.txt", "r") as archivo:
        for linea in archivo:
            nombre, materia, nota = linea.strip().split(",")
            print(f"Estudiante: {nombre} | Materia: {materia} | Nota: {nota}")
except FileNotFoundError:
    print("⚠️ No se encontraron notas registradas.")