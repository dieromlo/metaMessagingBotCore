import json

def cargarConfiguracion():
    try:
        with open("config.json", "r", encoding="utf-8") as archivoConfig:
            return json.load(archivoConfig)
    except FileNotFoundError:
        print("❌ Error: No encontré config.json")
        return None