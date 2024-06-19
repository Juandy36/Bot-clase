import discord
from discord.ext import commands
import random
import os
import requests 

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

# Define intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Crea un bot con el prefijo deseado
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

# Evento on_ready
@bot.event
async def on_ready():
    print(f'Logeado con el nombre: {bot.user} y con el Id: {bot.user.id})')
    print('------')


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)

@bot.command
async def Preguntar(ctx):
  
Organicos = {
    "MANZANAS": "Organicos", "PLATANOS": "Organicos", "NARANJAS": "Organicos",
    "FRESA": "Organicos", "UVAS": "Organicos", "MANGOS": "Organicos", "PERAS": "Organicos",
    "ESPINACAS": "Organicos", "ZANAHORIAS": "Organicos", "TOMATE": "Organicos", "LECHUGA": "Organicos",
    "PEPINO": "Organicos", "PIMIENTO": "Organicos", "BROCOLI": "Organicos", "ALBAHACA": "Organicos",
    "PEREJIL": "Organicos", "CILANTRO": "Organicos", "ROMERO": "Organicos", "TOMILLO": "Organicos",
    "AJO": "Organicos", "LECHE": "Organicos", "QUESO": "Organicos", "YOGUR": "Organicos",
    "MANTEQUILLA": "Organicos", "POLLO": "Organicos", "RES": "Organicos", "CERDO": "Organicos",
    "PESCADO": "Organicos", "PULPO": "Organicos", "CAMARON": "Organicos", "CANGREJO": "Organicos",
    "CALAMAR": "Organicos", "LENTEJA": "Organicos", "GARBANZOS": "Organicos", "FRIJOL": "Organicos",
    "GALLETAS": "Organicos", "GRANOLA": "Organicos", "CHIPS_VEGETARIANOS": "Organicos",
    "PAN": "Organicos", "PASTELES": "Organicos", "GALLETAS": "Organicos", "PASTELES": "Organicos",
    "JUGOS": "Organicos", "TE": "Organicos", "CAFE": "Organicos", "LECHE": "Organicos",
    "CREMAS": "Organicos", "LOCIONES": "Organicos", "JABONES": "Organicos", "CHAMPU": "Organicos",
    "ACONDICIONADORES": "Organicos", "ALIMENTOS_DE_MASCOTAS": "Organicos", "MASCOTAS": "Organicos"
}

Inorganicos = {
    "HIERRO": "Inorganicos", "COBRE": "Inorganicos", "ALUMINO": "Inorganicos", "ORO": "Inorganicos",
    "PLATA": "Inorganicos", "ZINC": "Inorganicos", "NIQUEL": "Inorganicos", "CUARZO": "Inorganicos",
    "CALCITA": "Inorganicos", "YESO": "Inorganicos", "MAGNETITA": "Inorganicos", "PIRITA": "Inorganicos",
    "FLUORITA": "Inorganicos", "CEMENTO": "Inorganicos", "CONCRETO": "Inorganicos", "LADRILLO": "Inorganicos",
    "VIDRIO": "Inorganicos", "CERAMICA": "Inorganicos", "ASFALTO": "Inorganicos", "TELEFONO": "Inorganicos",
    "COMPUTADORAS": "Inorganicos", "TELEVISORES": "Inorganicos", "FERTILIZANTES_QUIMICOS": "Inorganicos",
    "PESTICIDAS_QUIMICOS": "Inorganicos", "CLORO": "Inorganicos", "AMONIACO": "Inorganicos",
    "OLLA": "Inorganicos", "SARTENE": "Inorganicos", "CUCHILLO_INOXIDABLE": "Inorganicos",
    "REFRIGERADORES": "Inorganicos", "LAVADORAS": "Inorganicos", "MICROONDAS": "Inorganicos",
    "BATERIA_DE_LITIO": "Inorganicos", "BATERIA_ALCALINAS": "Inorganicos", "BATERIA_DE_PLOMO": "Inorganicos",
    "COMBUSTIBLE_FOSIL": "Inorganicos", "GAS_LICUADO_DE_PETROLEO": "Inorganicos"
}

# Lista de residuos aprovechables y no aprovechables
aprovechables = set(Organicos.keys())
no_aprovechables = set(Inorganicos.keys())

bot = commands.Bot(command_prefix='!')

@bot.command()
async def Preguntar(ctx, *, item: str):
    item = item.upper()
    if item in Organicos:
        tipo = "orgánico"
        cesta = "aprovechable" if item in aprovechables else "no aprovechable"
    elif item in Inorganicos:
        tipo = "inorgánico"
        cesta = "aprovechable" if item in aprovechables else "no aprovechable"
    else:
        await ctx.send(f"El item '{item}' no está en la lista.")
        return

    await ctx.send(f"El item '{item}' es {tipo} y es {cesta}.")

@bot.command()
async def Ejemplo(ctx):
    cosas = {
        "MANZANAS": "Organicos", "PLATANOS": "Organicos", "NARANJAS": "Organicos",
        "FRESA": "Organicos", "UVAS": "Organicos", "MANGOS": "Organicos", "PERAS": "Organicos",
        "ESPINACAS": "Organicos", "ZANAHORIAS": "Organicos", "TOMATE": "Organicos", "LECHUGA": "Organicos",
        "PEPINO": "Organicos", "PIMIENTO": "Organicos", "BROCOLI": "Organicos", "ALBAHACA": "Organicos",
        "PEREJIL": "Organicos", "CILANTRO": "Organicos", "ROMERO": "Organicos", "TOMILLO": "Organicos",
        "AJO": "Organicos", "LECHE": "Organicos", "QUESO": "Organicos", "YOGUR": "Organicos",
        "MANTEQUILLA": "Organicos", "POLLO": "Organicos", "RES": "Organicos", "CERDO": "Organicos",
        "PESCADO": "Organicos", "PULPO": "Organicos", "CAMARON": "Organicos", "CANGREJO": "Organicos",
        "CALAMAR": "Organicos", "LENTEJA": "Organicos", "GARBANZOS": "Organicos", "FRIJOL": "Organicos",
        "GALLETAS": "Organicos", "GRANOLA": "Organicos", "CHIPS_VEGETARIANOS": "Organicos",
        "PAN": "Organicos", "PASTELES": "Organicos", "GALLETAS": "Organicos", "PASTELES": "Organicos",
        "JUGOS": "Organicos", "TE": "Organicos", "CAFE": "Organicos", "LECHE": "Organicos",
        "CREMAS": "Organicos", "LOCIONES": "Organicos", "JABONES": "Organicos", "CHAMPU": "Organicos",
        "ACONDICIONADORES": "Organicos", "ALIMENTOS_DE_MASCOTAS": "Organicos", "MASCOTAS": "Organicos",
        "HIERRO": "Inorganicos", "COBRE": "Inorganicos", "ALUMINO": "Inorganicos", "ORO": "Inorganicos",
        "PLATA": "Inorganicos", "ZINC": "Inorganicos", "NIQUEL": "Inorganicos", "CUARZO": "Inorganicos",
        "CALCITA": "Inorganicos", "YESO": "Inorganicos", "MAGNETITA": "Inorganicos", "PIRITA": "Inorganicos",
        "FLUORITA": "Inorganicos", "CEMENTO": "Inorganicos", "CONCRETO": "Inorganicos", "LADRILLO": "Inorganicos",
        "VIDRIO": "Inorganicos", "CERAMICA": "Inorganicos", "ASFALTO": "Inorganicos", "TELEFONO": "Inorganicos",
        "COMPUTADORAS": "Inorganicos", "TELEVISORES": "Inorganicos", "FERTILIZANTES_QUIMICOS": "Inorganicos",
        "PESTICIDAS_QUIMICOS": "Inorganicos", "CLORO": "Inorganicos", "AMONIACO": "Inorganicos",
        "OLLA": "Inorganicos", "SARTENE": "Inorganicos", "CUCHILLO_INOXIDABLE": "Inorganicos",
        "REFRIGERADORES": "Inorganicos", "LAVADORAS": "Inorganicos", "MICROONDAS": "Inorganicos",
        "BATERIA_DE_LITIO": "Inorganicos", "BATERIA_ALCALINAS": "Inorganicos", "BATERIA_DE_PLOMO": "Inorganicos",
        "COMBUSTIBLE_FOSIL": "Inorganicos", "GAS_LICUADO_DE_PETROLEO": "Inorganicos"
    }
    

    for _ in range(10):
        cosa = random.choice(list(cosas.keys()))
        await ctx.send(cosa)

        @bot.command()
        async def contaminacion(ctx):
         await ctx.send(f'Hablamos de contaminación cuando en un entorno ingresan elementos o sustancias que normalmente no deberían estar en él y que afectan el equilibrio del ecosistema.')

@bot.command()
async def cuidado_ambiental(ctx):
    await ctx.send(f'No tires basura en las calles. Evita quemar basura, hojas y otros objetos, así como hacer fogatas en bosques o en plena ciudad. Riega las plantas durante la noche o muy temprano, cuando el Sol tarda más en evaporar el agua. {bot.user}!')

bot.run('token')
