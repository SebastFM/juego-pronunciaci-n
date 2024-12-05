import pygame
import random
import time
import speech_recognition as sp

niveles = {
    "español": {
        "facil": ["casa", "perro", "libro", "mesa", "agua"],
        "intermedio": ["computadora", "aventura", "musica", "planeta", "rojo"],
        "dificil": ["tecnologia", "inteligencia", "revolucionario", "extraordinario", "investigacion"]
    },
    "frances": {
        "facil": ["agenda", "ami", "souris"],
        "intermedio": ["ordinateur", "algorithme", "développeur"],
        "dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
    },
    "ingles": {
        "facil": ["cat", "dog", "house", "book", "tree"],
        "intermedio": ["computer", "adventure", "music", "planet", "green"],
        "dificil": ["technology", "intelligence", "revolutionary", "extraordinary", "investigation"]
    },
    "japones": {
        "facil": ["こんにちは", "はい", "猫", "犬", "本"],
        "intermedio": ["コンピュータ", "音楽", "先生", "学生", "友達"],
        "dificil": ["テクノロジー", "人工知能", "コミュニケーション", "イノベーション", "グローバリゼーション"]
    },
    "italiano": {
        "facil": ["casa", "ciao", "libro", "acqua", "sole"],
        "intermedio": ["computer", "musica", "viaggio", "amico", "stella"],
        "dificil": ["tecnologia", "intelligenza", "comunicazione", "innovazione", "rivoluzionario"]
    }
}

def elegir_idioma():
    print("Idiomas que puedes elegir:")
    for idioma in niveles.keys():
        print(f"- {idioma}")
    
    while True:
        idioma = input("Elige un idioma: ").lower()
        if idioma in niveles:
            return idioma
        print("Idioma no válido. Intenta de nuevo.")

def elegir_dificultad(idioma):
    print("Niveles de dificultad:")
    print("- facil")
    print("- intermedio")
    print("- dificil")
    
    while True:
        dificultad = input("Elige un nivel de dificultad: ").lower()
        if dificultad in niveles[idioma]:
            return dificultad
        print("Nivel de dificultad no válido. Intenta de nuevo.")

def obtener_palabra(idioma, dificultad):
    palabras = niveles[idioma][dificultad]
    return random.choice(palabras)

def reconocimiento_voz(idioma):
    language_codes = {
        "español": "es-ES",
        "frances": "fr-FR",
        "ingles": "en-US",
        "japones": "ja-JP",
        "italiano": "it-IT"
    }
    reconocedor = sp.Recognizer()
    microfono = sp.Microphone()
    
    try:
        with microfono as source:
            print("Pronuncia la palabra...")
            reconocedor.adjust_for_ambient_noise(source)
            audio = reconocedor.listen(source, timeout=5)
            palabra_dicha = reconocedor.recognize_google(audio, language=language_codes[idioma])
            return palabra_dicha.lower()
        
    except sp.UnknownValueError:
        print("No se detectó sonido, se marcará como incorrecto. Para la próxima habla :D .")
        return None
    except sp.RequestError:
        print("Error en el servicio de reconocimiento de voz.")
        return None

def jugar_pronunciacion():
    print("¡Bienvenido al juego de deletreo!")
    idioma = elegir_idioma()
    dificultad = elegir_dificultad(idioma)
    
    puntos = 0
    rondas = 5
    
    for ronda in range(rondas):
        palabra = obtener_palabra(idioma, dificultad)
        time.sleep(2)
        print(f"\nRonda {ronda + 1}: Deletrea la palabra: {palabra}")
        
        palabra_usuario = reconocimiento_voz(idioma)
        
        if palabra_usuario == palabra:
            puntos += 1
            print(f"¡Correcto! Puntos: {puntos}")
        else:
            print(f"Incorrecto. La palabra era: {palabra}")
    
    print(f"\nJuego terminado. Puntuación final: {puntos}/{rondas}")

if __name__ == "__main__":
    jugar_pronunciacion()