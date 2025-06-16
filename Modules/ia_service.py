import google.generativeai as genai
import csv
from dotenv import load_dotenv
import os

load_dotenv()  
API_KEY_GEMINI = os.getenv("API_KEY_GEMINI")
RUTA_HISTORIAL = "Data/historial_global.csv"

def dar_consejo(usuario):
    ultima = obtener_ultima_consulta(usuario)
    if not ultima:
        print("No se encontró una consulta previa. Hacé una consulta de clima primero.")
        return

    ciudad, fecha, temp, condicion, humedad, viento = ultima
    print(f"\nGenerando consejo de vestimenta para {ciudad} ({fecha})...")
    prompt = (
        f"Soy un asistente de vestimenta inteligente. El clima en {ciudad} es:\n"
        f"- Temperatura: {temp}°C\n"
        f"- Condición: {condicion}\n"
        f"- Humedad: {humedad}%\n"
        f"- Viento: {viento} km/h\n"
        "¿Qué ropa le recomendarías a una persona para hoy?, el texto va a ser enviado por consola de comandos de python por lo cual me gustaria que fuera breve y conciso, no más de 50 palabras.\n"
    )

    try:
        genai.configure(api_key=API_KEY_GEMINI)
        modelo = genai.GenerativeModel('models/gemini-1.5-flash')
        respuesta = modelo.generate_content(prompt)

        if respuesta.text:
            print("\n👕 Consejo de vestimenta:")
            print(respuesta.text.strip())
        else:
            print("La IA no generó un consejo. Revisá el prompt o los datos.")
    except Exception as e:
        print(f"Error con Gemini: {e}")

def obtener_ultima_consulta(usuario):
    try:
        with open(RUTA_HISTORIAL, mode='r', newline='') as archivo:
            lector = csv.reader(archivo)
            filas = [fila for fila in lector if fila and fila[0] == usuario]
            return filas[-1][1:] if filas else None
    except FileNotFoundError:
        return None
