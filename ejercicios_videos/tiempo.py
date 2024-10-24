import flet as ft
import aiohttp

weather_translations = {
    "clear sky": "cielo despejado",
    "few clouds": "algunas nubes",
    "scattered clouds": "nubes dispersas",
    "broken clouds": "nubosidad variable",
    "shower rain": "lluvia intermitente",
    "rain": "lluvia",
    "thunderstorm": "tormenta",
    "snow": "nieve",
    "mist": "neblina",
    "overcast clouds": "nubes",
    "light rain": "lluvia ligera",
    "moderate rain": "lluvia moderada",
    "heavy intensity rain": "lluvia intensa",
    "very heavy rain": "lluvia muy intensa",
    "extreme rain": "lluvia extrema",
    "freezing rain": "lluvia helada",
    "light intensity shower rain": "llovizna ligera",
    "heavy intensity shower rain": "llovizna intensa",
    "light snow": "nevada ligera",
    "heavy snow": "nevada intensa",
    "sleet": "aguanieve",
    "light shower sleet": "aguanieve ligera",
    "shower sleet": "aguanieve",
    "light rain and snow": "lluvia ligera y nieve",
    "rain and snow": "lluvia y nieve",
    "light shower snow": "nevada ligera",
    "shower snow": "nevada",
    "heavy shower snow": "nevada intensa",
    "fog": "niebla",
    "haze": "bruma",
    "smoke": "humo",
    "sand/dust whirls": "remolinos de arena/polvo",
    "sand": "arena",
    "dust": "polvo",
    "volcanic ash": "ceniza volcánica",
    "squalls": "chubascos",
    "tornado": "tornado"
}

# Ejemplo encontrado sobre el uso de la API de OpenWeatherMap para obtener el clima de una ciudad
async def get_weather(city):
    async with aiohttp.ClientSession() as session:
        # Reemplazar CODIGO_API por tu API Key de OpenWeatherMap pero no subirlo a GitHub
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=CODIGO_API&units=metric"
        async with session.get(url) as response:
            if response.status != 200:
                return f"Error: No se pudo obtener el clima para {city}. Código de estado: {response.status}"
            data = await response.json()
            if 'main' not in data or 'temp' not in data['main'] or 'weather' not in data or len(data['weather']) == 0:
                return f"Error: Datos inesperados recibidos para {city}. Respuesta: {data}"
            temp = data['main']['temp']
            description_en = data['weather'][0]['description']
            description_es = weather_translations.get(
                description_en, description_en)
            return f"Temperatura en {city}: {temp}°C con {description_es}"


async def main(page: ft.Page):
    page.title = "Aplicación del Clima"

    city_input = ft.TextField(label="Ingrese una ciudad")
    weather_text = ft.Text()

    async def get_weather_click(e):
        if not city_input.value:
            weather_text.value = "Por favor, ingrese un nombre de ciudad."
        else:
            weather_text.value = "Cargando..."
            page.update()
            try:
                weather_text.value = await get_weather(city_input.value)
            except Exception as ex:
                weather_text.value = f"Error inesperado: {str(ex)}"
        page.update()

    page.add(
        city_input,
        ft.ElevatedButton("Obtener clima", on_click=get_weather_click),
        weather_text
    )

ft.app(target=main)
