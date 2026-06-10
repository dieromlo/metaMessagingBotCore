import json

def cargarPlanes():
    try:
        with open("data/planes.json", "r", encoding="utf-8") as archivoPlan:
            return json.load(archivoPlan)
    except FileNotFoundError:
        return {}

def procesarMensaje(textoCliente):
    datosPlanes = cargarPlanes()
    mensajeLimpio = textoCliente.strip().lower()
    
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
                "Por favor, responde únicamente con el **NÚMERO** de la opción que te interesa consultar:\n\n"
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
        
        textoFullTigo = (
            "🚀 *Combos FullTigo disponibles para este mes:*\n\n"
            f"📱 *{duoFull['nombre']}*\n"
            f"• Incluye: {duoFull['descripcion']}\n"
            f"• Precio: {duoFull['precio']}\n"
            f"• Promo: {duoFull['promocion']}\n\n"
            f"📺 *{trioFull['nombre']}*\n"
            f"• Incluye: {trioFull['descripcion']}\n"
            f"• Precio: {trioFull['precio']}\n"
            f"• Promo: {trioFull['promocion']}\n\n"
            "💬 Si quieres contratar alguno de estos combos, escribe la palabra *Contratar*.\n"
            "🔙 Si deseas regresar al menú anterior, escribe *Inicio*."
        )
        return {"accion": "responder", "respuesta": textoFullTigo}

    elif mensajeLimpio == "2":
        hogarIndividual = datosPlanes["serviciosHogar"]["individual"]
        hogarDuo = datosPlanes["serviciosHogar"]["duo"]
        hogarTrio = datosPlanes["serviciosHogar"]["trio"]
        
        textoHogar = (
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
            "💬 Si quieres adquirir alguno de estos planes, escribe la palabra *Contratar*.\n"
            "🔙 Si deseas regresar al menú anterior, escribe *Inicio*."
        )
        return {"accion": "responder", "respuesta": textoHogar}

    elif mensajeLimpio == "3" or mensajeLimpio == "contratar":
        textoRequisitos = (
            "📄 *Datos necesarios para tu instalación:*\n\n"
            "Para agendar la instalación (la cual toma un tiempo estimado de 48 horas hábiles), "
            "necesitamos validar tus datos de forma rápida y segura. Por favor envíanos:\n\n"
            "1. Foto de tu cédula colombiana o PPT por ambos lados.\n"
            "2. Una foto tuya sosteniendo la cédula o PPT (de los hombros hacia arriba).\n"
            "3. Tu correo electrónico activo.\n"
            "4. Dirección exacta completa (o foto de la factura de EPM o PIN si haces recarga de luz).\n"
            "5. Números de contacto: Un número principal y uno adicional.\n\n"
            "⚠️ *Nota:* En un momento te enviaremos una imagen guía detallada. "
            "Apenas envíes los datos, la asesora *Delcy Romero* tomará el control para ingresar tu solicitud al sistema."
        )
        return {"accion": "enviarTextoEImagen", "respuesta": textoRequisitos}

    # 🛠️ Opción 4 actualizada con el texto oficial de tu mamá
    elif mensajeLimpio == "4":
        datosSoporte = datosPlanes["soporte"]
        textoSoporte = (
            f"💳 *Facturación y Soporte Técnico Tigo:*\n\n"
            f"Recuerda que, en nuestro Centro de Ayuda *{datosSoporte['centroAyuda']}* puede estar la información que necesitas 😊\n\n"
            f"*Si necesitas soporte técnico para tu hogar 🏠, te invitamos a llamar a nuestra Línea de Servicio al:*\n"
            f"- *{datosSoporte['lineaMovil']}* desde móviles Tigo\n"
            f"- *{datosSoporte['lineaFijaNacional']}* o *{datosSoporte['lineaFijaCorta']}* desde fijas Tigo\n"
            f"- *{datosSoporte['lineaLocal']}* desde fijos o móviles\n\n"
            f"🔒 *Para pagos seguros de facturas:* {datosSoporte['linkPago']}\n\n"
            f"🔙 Si deseas regresar al menú, escribe *Inicio*."
        )
        return {"accion": "responder", "respuesta": textoSoporte}

    else:
        textoError = (
            "❌ *Opción no válida.*\n\n"
            "Por favor, escribe únicamente el **NÚMERO** de la opción correspondiente (1 al 5) "
            "O escribe *Delcy* si deseas atención humana inmediata."
        )
        return {"accion": "error", "respuesta": textoError}