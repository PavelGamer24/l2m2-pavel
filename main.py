import random
import discord
from discord.ext import commands
import aiohttp

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def consejo(ctx):
    consejos = [
        "Usa transporte público o bicicleta para reducir las emisiones de CO2.",
        "Planta árboles y cuida las áreas verdes en tu comunidad.",
        "Reduce el consumo de plásticos de un solo uso.",
        "Ahorra energía apagando luces y electrodomésticos cuando no los uses.",
        "Recicla y separa tus residuos correctamente.",
        "Evita quemar basura o desechos, ya que liberan toxinas al aire.",
        "Utiliza productos de limpieza ecológicos y no tóxicos.",
        "Compra productos locales para reducir la huella de carbono del transporte.",
        "Usa bolsas reutilizables en lugar de bolsas de plástico.",
        "Reduce el consumo de carne y opta por una dieta más basada en plantas.",
        "Repara y reutiliza objetos en lugar de desecharlos.",
        "Instala paneles solares para aprovechar la energía renovable.",
        "Evita el uso de pesticidas y fertilizantes químicos en tu jardín.",
        "Participa en campañas de limpieza de ríos y playas.",
        "Educa a otros sobre la importancia de reducir la contaminación."
    ]
    consejo = random.choice(consejos)
    await ctx.send(f"**Consejo para reducir la contaminación:**\n{consejo}")

@bot.command()
async def contaminacion(ctx, pais: str):
    # URL de una API ficticia (reemplaza con una API real como OpenAQ o similar)
    api_url = f"https://api.contaminacion.com/v1/airquality?country={pais}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                calidad_aire = data.get("quality", "Desconocido")
                await ctx.send(f"La calidad del aire en {pais.capitalize()} es: **{calidad_aire}**")
            else:
                await ctx.send("No se pudo obtener la información de contaminación. Intenta de nuevo más tarde.")

bot.run("25cdc59cdc183095b22e5b652c14822bb582e07b6fa360b1e29632415afc8e4b")
