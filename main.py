import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
import asyncio


from youtube_dl import YoutubeDL
from pytube import YouTube

client = discord.Client() #define o cliente numa variavel
client = commands.Bot(command_prefix='$') # Seta o prefixo dos comandos como "$"

def devolverTitulo(url):
    yt = YouTube(url)
    return yt.title


@client.event
async def on_ready(): # quando ele inicia dispara esse evento
    texto = client.get_channel(750732431077801994)
    print("Estou pronto! Estou logado como {}".format(client.user))
    await texto.send("To online novamente!")

# ---------------------------- MÚSICA ----------------------------

@client.command(pass_context=True)
async def join(ctx): # para entrar na call
    canal = ctx.author.voice.channel
    if ctx.author.voice is None:
        await ctx.canal.send("Você não está em um canal de voz!")
    else: 
        await canal.connect()
            
@client.command(pass_context=True) #'pass context' faz o ctx ser passado na função abaixo
async def quit(ctx): # para sair da call
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.voice_client.disconnect()

@client.command(pass_context=True) #'pass context' faz o ctx ser passado na função abaixo
async def pause(ctx): # para sair da call
    await ctx.voice_client.pause()
    await ctx.send("Pausado!")

@client.command(pass_context=True) #'pass context' faz o ctx ser passado na função abaixo
async def resume(ctx): # para sair da call
    await ctx.voice_client.resume()
    await ctx.send("Continuando")

@client.command(pass_context=True) #'pass context' faz o ctx ser passado na função abaixo
async def stop(ctx): # para sair da call
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("Música finalizada!")


@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)
    canal = ctx.author.voice.channel

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send("O bot tocará: {}".format(devolverTitulo(url)))

arq = open("token.txt", "r") 
TOKEN = arq.readline()
arq.close()

client.run(TOKEN)