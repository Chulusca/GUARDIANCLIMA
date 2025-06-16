from Modules import auth
from Modules import weather_service
from Modules import history
from Modules import ia_service
from Utils import helpers

def mostrar_menu_acceso():
    while True:
        print("\n--- GUARDIÁN CLIMA ITBA ---")
        print("1. Iniciar Sesión")
        print("2. Registrar Nuevo Usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = auth.login()
            if usuario:
                mostrar_menu_principal(usuario)
        elif opcion == "2":
            usuario = auth.registrar()
            if usuario:
                mostrar_menu_principal(usuario)
        elif opcion == "3":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción inválida.")

def mostrar_menu_principal(usuario):
    while True:
        print(f"\n--- Bienvenido, {usuario} ---")
        print("1. Consultar clima")
        print("2. Ver historial personal")
        print("3. Ver estadísticas globales")
        print("4. Consejo IA: ¿Cómo me visto hoy?")
        print("5. Acerca de...")
        print("6. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            weather_service.consultar_clima(usuario)
        elif opcion == "2":
            history.ver_historial_personal(usuario)
        elif opcion == "3":
            history.estadisticas_globales()
        elif opcion == "4":
            ia_service.dar_consejo(usuario)
        elif opcion == "5":
            helpers.acerca_de_app()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
