# GuardiánClima ITBA

**Aplicación de clima y consejos personalizada**

---

## Descripción

GuardiánClima ITBA es una aplicación desarrollada para facilitar a los usuarios la consulta del clima y recibir consejos personalizados basados en sus búsquedas recientes. La app ofrece funcionalidades de registro seguro, consulta de clima en diferentes ciudades, historial personal de búsquedas, estadísticas globales de todos los usuarios y un asistente IA que brinda recomendaciones sobre cómo vestirse según el clima consultado.

---

## Funcionalidades principales

- **Registro y autenticación segura**: Los usuarios deben registrarse siguiendo pautas estrictas de seguridad para proteger su información.
- **Consulta del clima**: Permite obtener el pronóstico del clima en múltiples ciudades.
- **Historial personal**: Guarda y muestra el historial de búsquedas de clima del usuario.
- **Estadísticas globales**: Muestra estadísticas agregadas de todas las consultas realizadas por la comunidad.
- **Consejos personalizados con IA**: Basado en la última búsqueda, la IA recomienda cómo vestirse para el clima actual.

---

## Tecnologías utilizadas

- Lenguaje: Python
- Módulos principales: `auth`, `weather_service`, `history`, `ia_service`
- Gestión de datos: CSV para almacenamiento local de usuarios y búsquedas
- Otras herramientas: Consola interactiva para navegación por menús

---

## Instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/chulsuca/guardianclima-itba.git
   cd guardianclima-itba
   ```

2. Instalar dependencias (si las hubiera):

   ```bash
   pip install requests, google-generativeai, python-dotenv
   ```

3. Configurar las Variables de entorno:
   - Crea el archivo ".env"
   ```bash
      API_KEY_GEMINI = "TU-API-KEY" 
      API_KEY_CLIMA = "TU-API-KEY"
   ```

4. Ejecutar la aplicación:

   ```bash
   python main.py
   ```

---

## Uso

- Al iniciar la aplicación, se solicitará registro o inicio de sesión.
- Tras ingresar, el usuario podrá elegir opciones para consultar el clima, revisar su historial, consultar estadísticas o pedir consejos a la IA.
- Los datos de usuarios y búsquedas se almacenan localmente para mantener el historial y estadísticas.

---