import discord
from discord.ext import commands
import os, random
import requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Merhaba, ben bir botum")

@bot.command() 
async def check(ctx): # $check
    sayac = 0
    if ctx.message.attachments:
        sayac += 1
        #... kodu yazmaya devam edecegiz
        for attachment in ctx.message.attachments:
        #.... 1- resmi bilgisayarimiza kaydetmemiz gerekiyor
        #.... 2- get_class sinifina resmi gonderip sonucu alacagiz
            await attachment.save(f'./{sayac}_{attachment.filename}') #
            await ctx.send(get_class(model_path='./keras_model.h5', labels_path='./labels.txt', image_path=f'./{sayac}_{attachment.filename}'))
        f'./{sayac}_{attachment.filename}'
    else:
        await ctx.send("You did not upload an image!")
    

bot.run('Token')
