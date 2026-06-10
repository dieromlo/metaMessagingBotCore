from main import cargarConfiguracion
from flask import Flask, request, jsonify
import json
import requests  # 🚀 Nueva librería para enviar la respuesta a Meta
from src.botBrain import procesarMensaje

app = Flask(__name__)

# 🔑 Configuración de Credenciales de Meta
TOKEN_VERIFICACION = "RomeroDevGroupToken2026"

def enviarMensajeWhatsApp(telefonoCliente, textoRespuesta):
    config = cargarConfiguracion()  # necesitas importar esta función
    if not config:
        print("❌ No se pudo cargar config.json")
        return

    url = f"https://graph.facebook.com/v25.0/{config['phoneId']}/messages"
    
    headers = {
        "Authorization": f"Bearer {config['accessToken']}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": telefonoCliente,
        "type": "text",
        "text": {
            "preview_url": False,
            "body": textoRespuesta
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"📡 Respuesta de Meta al enviar: {response.status_code} - {response.text}")
        if response.status_code == 200:
            print(f"✅ Mensaje enviado a: {telefonoCliente}")
        else:
            print(f"❌ Error Meta: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error crítico enviando mensaje: {e}")

@app.route("/webhook", methods=["GET"])
def verificarWebhook():
    modo = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    reto = request.args.get("hub.challenge")

    if modo == "subscribe" and token == TOKEN_VERIFICACION:
        print("✅ ¡Webhook verificado con éxito por Meta!")
        return reto, 200
    else:
        print("❌ Intento de verificación fallido (Token incorrecto)")
        return "Prohibido", 403

@app.route("/webhook", methods=["POST"])
def recibirMensaje():
    datos = request.get_json()
    
    try:
        entrada = datos["entry"][0]["changes"][0]["value"]
        
        if "messages" in entrada:
            detallesMensaje = entrada["messages"][0]
            numeroCliente = detallesMensaje["from"]
            
            if detallesMensaje["type"] == "text":
                textoCliente = detallesMensaje["text"]["body"]
                print(f"💬 El cliente [{numeroCliente}] escribió: {textoCliente}")
                
                # 🧠 Conectamos con el cerebro del bot
                evaluacionBot = procesarMensaje(textoCliente)
                print(f"🤖 El cerebro del bot decidió: {evaluacionBot['accion']}")
                
                # 📢 ¡NUEVO! Le ordenamos al bot hablar usando su nueva función de envío
                enviarMensajeWhatsApp(numeroCliente, evaluacionBot['respuesta'])
                
    except Exception as e:
        print(f"❌ Error procesando mensaje entrante: {e}")

    return jsonify({"status": "exitoso"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)