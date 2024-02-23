# WeatherAlert-Notifier

Este proyecto utiliza la API de OpenWeatherMap para monitorear las condiciones meteorológicas locales y enviar alertas a través de Twilio cuando se detecta un clima adverso, como tormentas, lluvias intensas o nieve.

## Funcionalidades

- Consulta las condiciones meteorológicas locales utilizando la API de OpenWeatherMap.
- Detecta condiciones meteorológicas adversas, como tormentas, lluvias intensas o nieve.
- Envía alertas a través de mensajes de WhatsApp utilizando Twilio.
- Personaliza la configuración de alertas según tus preferencias.

## Uso

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
3. Configura tus credenciales de OpenWeatherMap y Twilio en el archivo `config.py`.
4. Ejecuta el script `weather_alert.py` para iniciar el monitoreo del clima y recibir alertas.

## Configuración

Antes de ejecutar el script, asegúrate de configurar correctamente tus credenciales de OpenWeatherMap y Twilio en el archivo `config.py`.

```python
# config.py

# Credenciales de OpenWeatherMap
OWM_API_KEY = 'TU_API_KEY_DE_OPENWEATHERMAP'

# Credenciales de Twilio
TWILIO_ACCOUNT_SID = 'TU_TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'TU_TWILIO_AUTH_TOKEN'
