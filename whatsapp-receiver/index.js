const express = require('express');
const app = express();
const PORT = 5000;

// Habilitamos la lectura de datos en formato JSON
app.use(express.json());

// Token secreto que inventamos para que Meta valide nuestro servidor
const TOKEN_VERIFICACION = "RomeroDevGroupToken2026";

// 🌐 RUTA GET: Validación de Meta
app.get('/webhook', (req, res) => {
    const modo = req.query['hub.mode'];
    const token = req.query['hub.verify_token'];
    const challenge = req.query['hub.challenge'];

    if (modo === 'subscribe' && token === TOKEN_VERIFICACION) {
        console.log("✅ ¡Webhook verificado con éxito por Meta!");
        res.status(200).send(challenge);
    } else {
        console.log("❌ Intento de verificación fallido");
        res.sendStatus(403);
    }
});

//  RUTA POST: Recepción de mensajes en tiempo real
app.post('/webhook', (req, res) => {
    const datos = req.body;

    console.log("📥 Datos recibidos desde Meta:");
    console.log(JSON.stringify(datos, null, 2));

    // Validamos que el paquete contenga un mensaje de WhatsApp
    try {
        const cambio = datos.entry[0].changes[0].value;
        if (cambio.messages) {
            const detalleMensaje = cambio.messages[0];
            const numeroCliente = detalleMensaje.from;

            if (detalleMensaje.type === 'text') {
                const textoCliente = detalleMensaje.text.body;
                console.log(`💬 El cliente [${numeroCliente}] escribió: "${textoCliente}"`);
                
                // TODO: Aquí conectaremos nuestro puente hacia Spring Boot o la IA a futuro
            }
        }
    } catch (error) {
        // Ignoramos notificaciones de estado (como confirmaciones de lectura)
    }

    res.status(200).json({ status: 'exitoso' });
});

// Encendemos el servidor en el puerto 5000
app.listen(PORT, () => {
    console.log(`🚀 Servidor receptor escuchando en el puerto ${PORT}`);
});