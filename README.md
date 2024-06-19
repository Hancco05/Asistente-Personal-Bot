# Asistente de Voz con Python

Este es un asistente de voz desarrollado en Python que utiliza tecnologías como OpenAI GPT-3, OpenWeatherMap y Wikipedia para realizar diversas tareas. Puedes interactuar con el asistente mediante comandos de voz.

## Características

1. **Abrir navegador**: Abre el navegador Microsoft Edge.
2. **Buscar en Wikipedia**: Realiza una búsqueda en Wikipedia y te proporciona un resumen.
3. **Clima, fecha y hora**: Te informa sobre la temperatura actual, la fecha y la hora.
4. **Buscar en ChatGPT**: Realiza una búsqueda en ChatGPT y te proporciona una respuesta.
5. **Cerrar el bot**: Cierra el asistente de voz.

## Requisitos

- Python 3.7 o superior
- `pip` (Python package installer)

## Instalación

1. **Clona el repositorio**:

    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd asistente
    ```

2. **Crea un entorno virtual**:

    ```sh
    python -m venv myassistant-env
    ```

3. **Activa el entorno virtual**:

    - En Windows:

        ```sh
        myassistant-env\Scripts\activate
        ```

    - En macOS/Linux:

        ```sh
        source myassistant-env/bin/activate
        ```

4. **Instala las dependencias**:

    ```sh
    pip install -r requirements.txt
    ```

5. **Configura las claves de API**:

    Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:

    ```plaintext
    OPENAI_API_KEY=tu_clave_api_de_openai
    WEATHER_API_KEY=tu_clave_api_de_openweathermap
    ```

## Uso

Para iniciar el asistente de voz, ejecuta el siguiente comando en la terminal:

```sh
python asistente.py
