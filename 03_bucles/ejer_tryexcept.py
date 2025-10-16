try: 
    numero = int(input('ingresa un numero: '))
    print(f'El numero es {numero}')
except ValueError:
    print("debes ingresar un numero valido")