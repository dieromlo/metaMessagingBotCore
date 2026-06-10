from pyngrok import ngrok

print("🚀 Abriendo túnel seguro hacia el puerto 5000...")
# Abrimos el túnel HTTP en el puerto 5000
urlPublica = ngrok.connect(5000)

print("\n" + "="*50)
print(f"✅ ¡TÚNEL ACTIVO CON ÉXITO!")
print(f"🔗 Tu URL pública es: {urlPublica.public_url}")
print("="*50 + "\n")

print("⚠️ Deja esta terminal abierta para mantener el bot conectado.")
# Esto mantiene el script corriendo para que no se cierre el túnel
ngrok.get_ngrok_process().block_until_closed()  