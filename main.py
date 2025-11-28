import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def whtweather(ctx):
    role_id = 1443444045966737428

    role = ctx.guild.get_role(role_id)

    if role in ctx.author.roles:
        await ctx.send(F"Окей Я рад что у вас есть роль {role}")
        await ctx.send("Вот актуальная погода:  В РАЗРАБОТКЕ")
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

bot.run('token')
