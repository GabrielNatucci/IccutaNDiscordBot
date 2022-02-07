import discord
import musica

# cogs = [musica]

# for i in range(len(cogs)):
#     cogs[i].setup

arq = open("token.txt", 'r')
TOKEN = arq.readline()
arq.close()

client = discord.Client()


@client.event
async def on_ready():
    print("Estou pronto! Estou logado como {}".format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        await message.channel.send('wolrd!')


async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Seja bem vindo ao to {0.name}, {1.mention}'.format(guild ,member)
        await guild.system_channel.send(to_send)

client.run(TOKEN)