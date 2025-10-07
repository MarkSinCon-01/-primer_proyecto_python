lista = list((2,3,0))
tupla = tuple((2,1,0))
conjunto = set((2, 1, 0))
diccionario = dict(((2, "dos"), (1, "uno"), (0, "cero")))

for iterador in lista:
    print(iterador)

for iterador in tupla:
    print(iterador)
    
for iterador in conjunto:
    print(iterador)
    
for iterador in diccionario:
    print(iterador)
    
for iterador in diccionario.values():
    print(iterador)

for iterador in diccionario.items():
    print(iterador)
    