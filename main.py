from config import cargarConfiguracion
import requests

def enviarMensajePlantillaReal(numeroDestino):
    config = cargarConfiguracion()
    if not config:
        return

    urlApi = f"https://graph.facebook.com/v25.0/{config['phoneId']}/messages"
    
    cabeceras = {
        "Authorization": f"Bearer {config['accessToken']}",
        "Content-Type": "application/json"
    }
    
    cuerpoMensaje = {
        "messaging_product": "whatsapp",
        "to": numeroDestino,
        "type": "template",
        "template": {
            "name": "jaspers_market_order_confirmation_v1",
            "language": {
                "code": "en_US"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": "Juan Diego"},
                        {"type": "text", "text": "987654"},
                        {"type": "text", "text": "30 de Mayo, 2026"}
                    ]
                }
            ]
        }
    }

    print("🚀 Conectando con Romero Development Group...")
    respuestaApi = requests.post(urlApi, headers=cabeceras, json=cuerpoMensaje)
    
    if respuestaApi.status_code == 200:
        print("✅ ¡Petición aceptada y enviada con éxito por Meta!")
        print("Detalle del mensaje:", respuestaApi.json())
    else:
        print(f"❌ Error API Meta: {respuestaApi.status_code}")
        print(f"Detalle: {respuestaApi.text}")

if __name__ == "__main__":
    miCelular = "573002532832"
    enviarMensajePlantillaReal(miCelular)