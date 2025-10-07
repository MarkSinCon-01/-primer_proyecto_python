nota = float(input("Introduzca su nota: "))
if 0 <= nota and nota < 5:
    print("esta suspendido, F")
elif 5 <= nota and nota <7:
    print("Aprovado")
elif 7 <= nota and nota <9:
    print("Notable")
elif 9 <= nota and nota <10:
    print("Sobresaliente")
else:
    print("Nota fuera de rango") 