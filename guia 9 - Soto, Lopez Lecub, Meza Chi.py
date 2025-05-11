#Soto, Juan Bautista, Lopez Lecube, Lautaro, Meza Chiesa, Aylén
import random

# Variables globales
montos = []
fecha = []
nombre = []

# Generar las ventas de cada mes en una lista
def generar_monto():
    return [random.randint(50000, 300000) for _ in range(500)]

# Generar días aleatorios (solo días del 1 al 31)
def generar_fecha():
    return [f"{random.randint(1, 31)}" for _ in range(500)]

# Generar nombres aleatorios
def generar_nombre():
    nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Lucía", "Miguel", "Elena"]
    return [random.choice(nombres) for _ in range(500)]

# Mostrar las ventas
def mostrar_ventas():
    for i in range(len(montos)):
        print(f"Fecha: {fecha[i]} Montos: {montos[i]} Nombre: {nombre[i]}")

# Ordenar las ventas usando Shell Sort
def ordenar_monto():
    gap = len(montos) // 2
    c = 0
    while gap > 0:
        c+= 1
        for i in range(gap, len(montos)):
            temp_venta = montos[i]
            temp_fecha = fecha[i]
            temp_nombre = nombre[i]
            j = i
            while j >= gap and montos[j - gap] > temp_venta:
                montos[j] = montos[j - gap]
                fecha[j] = fecha[j - gap]
                nombre[j] = nombre[j - gap]
                j -= gap
            montos[j] = temp_venta
            fecha[j] = temp_fecha
            nombre[j] = temp_nombre
        gap //= 2  #Reducir el gap
    return c
        
# Ordenar las ventas por fecha usando Shell Sort
def ordenar_fecha():
    gap = len(fecha) // 2  # Usar división entera para calcular el gap
    c = 0
    while gap > 0:
        c+= 1
        for i in range(gap, len(fecha)):
            temp_venta = montos[i]
            temp_fecha = fecha[i]
            temp_nombre = nombre[i]
            j = i
            while j >= gap and int(fecha[j - gap]) > int(temp_fecha):
                montos[j] = montos[j - gap]
                fecha[j] = fecha[j - gap]
                nombre[j] = nombre[j - gap]
                j -= gap
            montos[j] = temp_venta
            fecha[j] = temp_fecha
            nombre[j] = temp_nombre
        gap //= 2  # Reducir el gap
    return c
# Mostrar las ventas ordenadas por fecha
def mostrar_ventas_ordenadas_fecha():
    print("Ventas ordenadas por fecha: ")
    for i in range(len(montos)):
        print(f"Fecha: {fecha[i]} Montos: {montos[i]} Nombre: {nombre[i]}")

# Mostrar las ventas ordenadas por monto
def mostrar_ventas_ordenadas_por_monto():
    print("Ventas ordenadas por monto:")
    for i in range(len(montos)):
        print(f"Fecha: {fecha[i]} Montos: {montos[i]} Nombre: {nombre[i]}")
 
# Inicializar las listas
montos = generar_monto() 
fecha = generar_fecha()
nombre = generar_nombre()

# Solicitar al usuario cómo desea ordenar las ventas
opcion = input("¿Cómo desea ordenar las ventas? (1: por fecha, 2: por monto): ")

if opcion == "1":
    ordenar_fecha()
    mostrar_ventas_ordenadas_fecha()
elif opcion == "2":    
    ordenar_monto()
    mostrar_ventas_ordenadas_por_monto()
else:
    print("Opción no válida.")