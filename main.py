import requests
from twilio.rest import Client
import os

latitud = "39.985782"
longitud = "4.014402"

website = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
      "lat": latitud,
      "lon": longitud,
      "timezone": "Europe/Madrid",
      "exclude": "alerts,current,minutely,daily",
      "appid": "bac2e6b0b08ce3fa646a40e3a2658c58"
}

response = requests.get(website, params=parameters)
response.raise_for_status()
data = response.json()

pro = data["hourly"][0]["weather"][0]["id"]

tiempo_horas = data["hourly"][:12]
tiempo = False

for hora in tiempo_horas:
    if hora["weather"][0]["id"] < 700:
        tiempo = True
        break

if tiempo:
    # Token de autenticación de Twilio
    account_sid = "YOUR_TWILIO_ACCOUNT_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"

    # Crea una instancia del cliente Twilio
    client = Client(account_sid, auth_token)

    # Cuerpo del mensaje con información meteorológica
    mensaje = "¡Atención! Se espera mal tiempo en las próximas horas."

    # Envía el mensaje de WhatsApp
    message = client.messages.create(
        body=mensaje,
        from_='whatsapp:+17408072714',
        to='whatsapp:+34618307559'
    )

    print("Mensaje enviado con éxito:", message.sid)
else:
    print("El tiempo parece estar bien en las próximas horas.")
