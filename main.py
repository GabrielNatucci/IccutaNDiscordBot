import discord
from discord.ext import commands
import musica

client = discord.Client() #define o cliente numa variavel
client = commands.Bot(command_prefix='$')

arq = open("token.txt", 'r') 
TOKEN = arq.readline()
arq.close()

@client.event
async def on_ready(): # quando ele inicia dispara esse evento
    print("Estou pronto! Estou logado como {}".format(client.user))

@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("Você não está em um canal de voz!")
    canal = ctx.author.voice.channel
    if ctx.voice_client is None:
        await canal.connect()

@client.command(pass_context=True) #'pass context' faz o ctx ser passado na função abaixo
async def desconectar(ctx):
    await ctx.voice_client.disconnect()


client.run(TOKEN)
