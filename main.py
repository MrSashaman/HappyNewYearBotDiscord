import requests
import discord
from discord import app_commands
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
API_KEY = 'api'

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Мы вошли как {bot.user}!')

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('pong')

@bot.tree.command(name="weather")
async def weather(interaction: discord.Interaction):
    role_id = 1443444045966737428
    role = interaction.guild.get_role(role_id)

    if role in interaction.user.roles:
        city = "Петропавловск-Камчатский"
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'

        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            # Вместо нескольких send_message, объединим все в один
            weather_message = (f"Вот актуальная погода в {city}:\n"
                               f"Температура: {temp}°C\n"
                               f"Описание: {weather_description}\n"
                               f"Влажность: {humidity}%\n"
                               f"Скорость ветра: {wind_speed} м/с")

            await interaction.response.send_message(weather_message)
        else:
            await interaction.response.send_message("Не удалось получить данные о погоде.")
    else:
        await interaction.response.send_message("У вас нет этой роли.")


@bot.tree.command(name="checkrole")
async def checkrole(interaction: discord.Interaction):
    role_id = 1443444045966737428
    role = interaction.guild.get_role(role_id)

    if role in interaction.user.roles:
        # Создаем сообщение с картинкой в одном ответе
        await interaction.response.send_message(
            f"Окей Я рад что у вас есть роль {role}\nВот картинка:",
            file=discord.File("avarter.png")
        )
    else:
        await interaction.response.send_message("У вас нет этой роли.")


bot.run('token')
