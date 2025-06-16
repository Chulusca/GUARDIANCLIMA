import csv
from collections import Counter, defaultdict

RUTA_HISTORIAL = "Data/historial_global.csv"

def ver_historial_personal(usuario):
    ciudad = input("Ingrese el nombre de la ciudad: ").strip().lower()
    try:
        with open(RUTA_HISTORIAL, mode='r', newline='') as archivo:
            lector = csv.reader(archivo)
            encontrados = [
                fila for fila in lector
                if fila and fila[0] == usuario and fila[1].lower() == ciudad
            ]
    except FileNotFoundError:
        print("No hay historial aún.")
        return

    if not encontrados:
        print("No hay consultas guardadas para esa ciudad.")
    else:
        print(f"\nHistorial de {usuario} en {ciudad.title()}:")
        for fila in encontrados:
            print(f"- {fila[2]} | {fila[3]}°C | {fila[4]} | Humedad: {fila[5]}% | Viento: {float(fila[6]):.1f} km/h")

def estadisticas_globales():
    try:
        with open(RUTA_HISTORIAL, mode='r', newline='') as archivo:
            lector = csv.reader(archivo)
            datos = list(lector)
    except FileNotFoundError:
        print("No hay historial aún.")
        return

    if not datos:
        print("Historial vacío.")
        return

    ciudades = [fila[1] for fila in datos]
    temperaturas = [float(fila[3]) for fila in datos]

    ciudad_mas_consultada = Counter(ciudades).most_common(1)[0]
    total_consultas = len(datos)
    temp_promedio = sum(temperaturas) / total_consultas

    print("\n📊 Estadísticas globales:")
    print(f"- Ciudad más consultada: {ciudad_mas_consultada[0]} ({ciudad_mas_consultada[1]} veces)")
    print(f"- Total de consultas realizadas: {total_consultas}")
    print(f"- Temperatura promedio: {temp_promedio:.2f} °C")
