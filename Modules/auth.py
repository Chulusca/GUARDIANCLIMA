import csv
import os
import re

RUTA_USUARIOS = "Data/usuarios_simulados.csv"
CRITERIOS = {
    "longitud": lambda p: len(p) >= 8,
    "mayúsculas": lambda p: any(c.isupper() for c in p),
    "minúsculas": lambda p: any(c.islower() for c in p),
    "números": lambda p: any(c.isdigit() for c in p),
    "especiales": lambda p: re.search(r"[!@#$%^&*(),.?\":{}|<>]", p)
}

def validar_contraseña(passwd):
    errores = []
    for nombre, regla in CRITERIOS.items():
        if not regla(passwd):
            errores.append(nombre)
    return errores

def registrar():
    print("\n--- Registro de Usuario ---")
    username = input("Ingrese un nuevo nombre de usuario: ").strip()

    if usuario_existe(username):
        print("Este nombre de usuario ya está registrado.")
        return None

    while True:
        password = input("Ingrese una contraseña segura: ").strip()
        errores = validar_contraseña(password)
        if errores:
            print(f"\nTu contraseña no cumple con: {', '.join(errores)}.")
            print("Recomendaciones: al menos 8 caracteres, incluir mayúsculas, minúsculas, números y símbolos especiales.\n")
        else:
            guardar_usuario(username, password)
            print("Registro exitoso.")
            return username

def login():
    print("\n--- Inicio de Sesión ---")
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    try:
        with open(RUTA_USUARIOS, mode='r', newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila == [username, password]:
                    print("Inicio de sesión exitoso.")
                    return username
        print("Usuario o contraseña incorrectos.")
        return None
    except FileNotFoundError:
        print("Aún no hay usuarios registrados.")
        return None

def usuario_existe(username):
    if not os.path.exists(RUTA_USUARIOS):
        return False
    with open(RUTA_USUARIOS, mode='r', newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[0] == username:
                return True
    return False

def guardar_usuario(username, password):
    os.makedirs(os.path.dirname(RUTA_USUARIOS), exist_ok=True)
    with open(RUTA_USUARIOS, mode='a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([username, password])
