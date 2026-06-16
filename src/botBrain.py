import json
import unicodedata

def normalizarTexto(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

def cargarPlanes():
    try:
        with open("data/planes.json", "r", encoding="utf-8") as archivoPlan:
            return json.load(archivoPlan)
    except FileNotFoundError:
        return {}

def procesarMensaje(textoCliente):
    datosPlanes = cargarPlanes()
    mensajeLimpio = normalizarTexto(textoCliente)
    
    if mensajeLimpio in ["5", "delcy", "asesor", "humano", "persona"]:
        return {
            "accion": "transferirADelcy",
            "respuesta": (
                "¡Claro que sí! Entiendo que prefieres una atención personalizada. 👩‍💼\n\n"
                "En este momento le estoy notificando a *Delcy Romero* para que tome tu caso de forma prioritaria. "
                "Ella revisará el chat en unos instantes. ¡Que tengas un feliz día! ☀️"
            )
        }

    if mensajeLimpio in ["hola", "buenos dias", "buenas tardes", "buenas noches", "inicio", "menu"]:
        return {
            "accion": "mostrarMenu",
            "respuesta": (
                "¡Hola! Te saluda el Asistente Virtual de *Delcy Romero*, asesora experta de ventas de Tigo Colombia 🇨🇴.\n\n"
                "Estoy aquí para darte información inmediata y agilizar tu proceso. "
                "Por favor, responde únicamente con el *NÚMERO* de la opción que te interesa consultar:\n\n"
                "1️⃣ Combos FullTigo (Internet Hogar + Celular en una sola factura) 🚀\n"
                "2️⃣ Planes de Internet o TV Individuales para la Casa 🏠\n"
                "3️⃣ Requisitos para realizar mi instalación 📄\n"
                "4️⃣ Consultar mi factura o Soporte Técnico 💳\n"
                "5️⃣ Hablar directamente con la asesora Delcy 👩"
            )
        }

    if mensajeLimpio == "1":
        duoFull = datosPlanes["fullTigo"]["duoFull"]
        trioFull = datosPlanes["fullTigo"]["trioFull"]
        return {
            "accion": "responder",
            "respuesta": (
                "🚀 *Combos FullTigo disponibles para este mes:*\n\n"
                f"📱 *{duoFull['nombre']}*\n"
                f"• Incluye: {duoFull['descripcion']}\n"
                f"• Precio: {duoFull['precio']}\n"
                f"• Promo: {duoFull['promocion']}\n\n"
                f"📺 *{trioFull['nombre']}*\n"
                f"• Incluye: {trioFull['descripcion']}\n"
                f"• Precio: {trioFull['precio']}\n"
                f"• Promo: {trioFull['promocion']}\n\n"
                "💬 Si quieres contratar alguno, escribe *Contratar*.\n"
                "🔙 Para regresar al menú escribe *Inicio*."
            )
        }

    elif mensajeLimpio == "2":
        hogarIndividual = datosPlanes["serviciosHogar"]["individual"]
        hogarDuo = datosPlanes["serviciosHogar"]["duo"]
        hogarTrio = datosPlanes["serviciosHogar"]["trio"]
        return {
            "accion": "responder",
            "respuesta": (
                "🏠 *Planes de Internet Residencial disponibles:*\n\n"
                f"🌐 *{hogarIndividual['nombre']}*\n"
                f"• Precio: {hogarIndividual['precio']}\n"
                f"• Promo: {hogarIndividual['promocion']}\n\n"
                f"👥 *{hogarDuo['nombre']}*\n"
                f"• Incluye: {hogarDuo['descripcion']}\n"
                f"• Precio: {hogarDuo['precio']}\n"
                f"• Promo: {hogarDuo['promocion']}\n\n"
                f"🏢 *{hogarTrio['nombre']}*\n"
                f"• Incluye: {hogarTrio['descripcion']}\n"
                f"• Precio: {hogarTrio['precio']}\n\n"
                "💬 Si quieres adquirir alguno, escribe *Contratar*.\n"
                "🔙 Para regresar al menú escribe *Inicio*."
            )
        }

    elif mensajeLimpio in ["3", "contratar"]:
        return {
            "accion": "enviarTextoEImagen",
            "respuesta": (
                "📄 *Datos necesarios para tu instalación:*\n\n"
                "Para agendar la instalación (48 horas hábiles aprox.), necesitamos:\n\n"
                "1. Foto de tu cédula colombiana o PPT por ambos lados.\n"
                "2. Foto tuya sosteniendo la cédula (hombros hacia arriba).\n"
                "3. Tu correo electrónico activo.\n"
                "4. Dirección exacta completa (o foto de factura EPM o PIN de recarga).\n"
                "5. Un número principal y uno adicional de contacto.\n\n"
                "⚠️ *Nota:* En un momento te enviamos una imagen guía. "
                "La asesora *Delcy Romero* tomará el control para ingresar tu solicitud."
            )
        }

    elif mensajeLimpio == "4":
        datosSoporte = datosPlanes["soporte"]
        return {
            "accion": "responder",
            "respuesta": (
                f"💳 *Facturación y Soporte Técnico Tigo:*\n\n"
                f"En nuestro Centro de Ayuda *{datosSoporte['centroAyuda']}* puede estar la info que necesitas 😊\n\n"
                f"*Soporte técnico para tu hogar 🏠:*\n"
                f"- *{datosSoporte['lineaMovil']}* desde móviles Tigo\n"
                f"- *{datosSoporte['lineaFijaNacional']}* o *{datosSoporte['lineaFijaCorta']}* desde fijas Tigo\n"
                f"- *{datosSoporte['lineaLocal']}* desde fijos o móviles\n\n"
                f"🔒 *Pagos seguros:* {datosSoporte['linkPago']}\n\n"
                "🔙 Para regresar al menú escribe *Inicio*."
            )
        }

    else:
        return {
            "accion": "error",
            "respuesta": (
                "❌ *Opción no válida.*\n\n"
                "Escribe únicamente el *NÚMERO* de la opción (1 al 5) "
                "o escribe *Delcy* para atención humana inmediata."
            )
        }