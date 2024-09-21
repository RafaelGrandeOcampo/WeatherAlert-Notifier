import requests
from twilio.rest import Client
from config import OWM_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_FROM, WHATSAPP_TO, LATITUD, LONGITUD, WEATHER_API_URL

# OpenWeatherMap API endpoint
# Utilizando la URL, latitud y longitud desde el archivo config
weather_api_url = WEATHER_API_URL

# Parameters for the weather API request
parameters = {
    "lat": LATITUD,
    "lon": LONGITUD,
    "exclude": "alerts,current,minutely,daily",
    "appid": OWM_API_KEY
}

try:
    # Fetch weather data from OpenWeatherMap
    response = requests.get(weather_api_url, params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract weather information for the next 12 hours
    pro = data["hourly"][0]["weather"][0]["id"]
    tiempo_horas = data["hourly"][:12]
    mal_tiempo = False

    # Check if bad weather (id < 700) is predicted in the next 12 hours
    for hora in tiempo_horas:
        if hora["weather"][0]["id"] < 700:
            mal_tiempo = True
            break

    if mal_tiempo:
        # Initialize Twilio client with SID and token
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Message to be sent via WhatsApp
        mensaje = "¡Atención! Se espera mal tiempo en las próximas horas."

        # Send WhatsApp message
        message = client.messages.create(
            body=mensaje,
            from_=TWILIO_WHATSAPP_FROM,  # Use the variable from config
            to=WHATSAPP_TO  # Use the variable from config
        )

        print("Mensaje enviado con éxito:", message.sid)
    else:
        print("El tiempo parece estar bien en las próximas horas.")

except requests.exceptions.RequestException as e:
    print(f"Error al obtener los datos del tiempo: {e}")
except Exception as e:
    print(f"Se produjo un error: {e}")

    print("Mensaje enviado con éxito:", message.sid)
else:
    print("El tiempo parece estar bien en las próximas horas.")
