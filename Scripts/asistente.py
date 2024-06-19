import speech_recognition as sr
import pyttsx3
import pyautogui
import wikipedia
import openai
import json
import os
import datetime
import requests
import sys

# Configurar la síntesis de voz
engine = pyttsx3.init()

# Configurar tu clave de API de OpenAI
openai.api_key = os.getenv('codee')

# Configurar archivo de caché
CACHE_FILE = 'gpt_cache.json'

# Cargar caché
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'r') as f:
        cache = json.load(f)
else:
    cache = {}

def save_cache():
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='es-ES')
            print(f"Tú dijiste: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Lo siento, no te entendí. ¿Puedes repetirlo?")
            return ""
        except sr.RequestError as e:
            print(f"Error de solicitud: {e}")
            speak("Parece que hay un problema con el servicio de reconocimiento de voz.")
            return ""

def chat_with_gpt(prompt):
    if prompt in cache:
        return cache[prompt]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message['content'].strip()
        cache[prompt] = answer
        save_cache()
        return answer
    except Exception as e:
        print(f"Error al comunicarse con GPT: {e}")
        return "Lo siento, no puedo responder eso en este momento."

def get_weather():
    api_key = "codee"  # Reemplaza esto con tu API key de OpenWeatherMap
    city = "Santiago"  # Reemplaza esto con tu ciudad
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            return f"La temperatura en {city} es de {temp} grados Celsius con {weather_desc}."
        else:
            return "No se pudo obtener el clima en este momento."
    except Exception as e:
        return f"Error al obtener el clima: {e}"

def respond(command):
    if "wikipedia" in command or "2" in command:
        speak("¿Qué quieres buscar en Wikipedia?")
        query = listen()
        results = wikipedia.summary(query, sentences=2, lang='es')
        speak("Según Wikipedia")
        speak(results)
    elif "abrir navegador" in command or "1" in command:
        pyautogui.hotkey('win', 'r')
        pyautogui.write('msedge\n')
        speak("Abriendo Microsoft Edge")
    elif "temperatura" in command or "día" in command or "hora" in command or "3" in command:
        now = datetime.datetime.now()
        weather = get_weather()
        speak(f"Hoy es {now.strftime('%A %d %B %Y')} y son las {now.strftime('%H:%M')}. {weather}")
    elif "buscar en chatgpt" in command or "4" in command:
        speak("¿Qué quieres buscar en ChatGPT?")
        query = listen()
        response = chat_with_gpt(query)
        speak(response)
    elif "cerrar" in command or "cerrar el bot" in command or "5" in command:
        speak("Cerrando el bot. Hasta luego.")
        sys.exit()
    else:
        speak("No entendí la opción. Por favor, di una de las opciones: abrir navegador, buscar en Wikipedia, temperatura, día y hora, buscar en ChatGPT, o cerrar el bot.")

if __name__ == "__main__":
    # Saludar y presentar opciones
    speak("Hola, soy tu asistente. Estas son tus opciones: 1) Abrir el navegador Microsoft Edge, 2) Buscar en Wikipedia, 3) Saber la temperatura, día y hora, 4) Buscar en ChatGPT, 5) Cerrar el bot. Por favor, di el número de la opción o su descripción.")
    while True:
        command = listen()
        if command:
            respond(command)
