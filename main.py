import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
API_KEY = 'апи'

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def weather(ctx):
    role_id = 1443444045966737428
    role = ctx.guild.get_role(role_id)

    if role in ctx.author.roles:
        city = "Петропавловск-Камчатский"
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'

        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            await ctx.send(f"Вот актуальная погода в {city}:")
            await ctx.send(f"Температура: {temp}°C\n"
                           f"Описание: {weather_description}\n"
                           f"Влажность: {humidity}%\n"
                           f"Скорость ветра: {wind_speed} м/с")
        else:
            await ctx.send("Не удалось получить данные о погоде.")
    else:
        await ctx.send("У вас нет этой роли.")

@bot.command()
async def checkrole(ctx):
    role_id = 1443444045966737428

    role = ctx.guild.get_role(role_id)

    if role in ctx.author.roles:
        await ctx.send(F"Окей Я рад что у вас есть роль {role}")
        await ctx.send("Вот картинка:", file=discord.File("avarter.png"))
    else:
        await ctx.send("У вас нет этой роли.")

bot.run('токен')
