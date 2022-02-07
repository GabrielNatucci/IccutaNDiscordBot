import discord
from discord.ext import commands
import youtube_dl

# ainda não fiz a implementação da música

class musica(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice == "none":
            await ctx.send("Você não está um canal de voz!")
 
def setup(client):
    client.add_cog(musica(client))