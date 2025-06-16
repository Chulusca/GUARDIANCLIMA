acerca_de = """
GUARDIÁNCLIMA ITBA - Aplicación de clima y consejos

Una aplicación desarrollada por estudiantes del ingreso del ITBA para facilitarle la vida a los usuarios a la hora de consultar el clima y recibir sugerencias útiles.

FUNCIONALIDADES PRINCIPALES:
  - Consultar el clima actual de cualquier ciudad.
  - Ver el historial de búsquedas personales.
  - Visualizar estadísticas globales de uso y clima consultado por todos los usuarios.
  - Pedir consejos personalizados a una IA basada en la última búsqueda realizada.

USO DEL MENÚ:
Al iniciar la aplicación, se muestra el Menú de Acceso, donde el usuario puede:
  - Registrarse: creando un usuario nuevo que cumpla con criterios estrictos de seguridad en la contraseña.
  - Iniciar sesión: para acceder a todas las funcionalidades mencionadas anteriormente.
  - Salir: cerrar la aplicación.

DESCRIPCIÓN TÉCNICA:
  - Registro de usuarios:
    Se simula la creación de usuarios con validación de contraseñas que exige:
      • Mínimo 8 caracteres
      • Al menos una mayúscula, una minúscula y un número
    Se alienta a usar contraseñas robustas para mayor seguridad.

  - Almacenamiento:
    Las credenciales se guardan de forma simulada e **insegura** en un archivo CSV.
    ⚠ Se advierte que este método **no es seguro en la vida real**.
    Se recomienda el uso de técnicas como el *hashing* con algoritmos como bcrypt o Argon2.

  - Clima e historial:
    Los datos meteorológicos se obtienen a través de un servicio simulado (o real si se conecta una API).
    Las búsquedas se registran en un historial personal y en un archivo global (`historial_global.csv`).

  - Estadísticas:
    A partir del historial global, se generan estadísticas agregadas por ciudad, uso por día, etc.
    Estos datos se exportan como CSV para ser utilizados en visualizaciones gráficas externas.

  - IA de Consejos:
    Se utiliza un sistema de IA que, en base al último clima consultado, brinda recomendaciones de vestimenta u otros consejos útiles.

INFORMACIÓN DEL EQUIPO:
  - Desarrolladores: Tomas Czernuszka, Juan Cruz Putallaz, Matias Carbone, Bautista Gonzales y Lucas Nieva.
  - Nombre del grupo: TecnoClima

¡Gracias por usar GUARDIÁNCLIMA ITBA!

"""

def acerca_de_app():
    print(acerca_de)
    input("\nPresione Enter para continuar...")
