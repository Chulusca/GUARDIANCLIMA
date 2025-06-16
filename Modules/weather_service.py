import requests
import csv
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  
API_KEY_GEMINI = os.getenv("API_KEY_CLIMA")
RUTA_HISTORIAL = "Data/historial_global.csv"

def consultar_clima(usuario):
    ciudad = input("Ingrese el nombre de la ciudad: ").strip()
    datos = obtener_clima_ciudad(ciudad)

    if datos:
        temperatura = datos["main"]["temp"]
        sensacion = datos["main"]["feels_like"]
        humedad = datos["main"]["humidity"]
        descripcion = datos["weather"][0]["description"].capitalize()
        viento = datos["wind"]["speed"] * 3.6  # m/s a km/h

        print(f"\nClima en {ciudad.title()}:")
        print(f"🌡️  Temp: {temperatura} °C (Sensación: {sensacion} °C)")
        print(f"💧 Humedad: {humedad}%")
        print(f"🌬️  Viento: {viento:.1f} km/h")
        print(f"☁️  Condición: {descripcion}")

        guardar_en_historial(usuario, ciudad, temperatura, descripcion, humedad, viento)

def obtener_clima_ciudad(ciudad):
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
        return None
    except requests.exceptions.RequestException:
        print("No se pudo conectar con la API del clima.")
        return None

def guardar_en_historial(usuario, ciudad, temp, condicion, humedad, viento):
    os.makedirs(os.path.dirname(RUTA_HISTORIAL), exist_ok=True)
    with open(RUTA_HISTORIAL, mode="a", newline="") as archivo:
        escritor = csv.writer(archivo)
        ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        escritor.writerow([usuario, ciudad, ahora, temp, condicion, humedad, viento])
        print("✔️ Consulta guardada en el historial.")
