import discord
import os

client = discord.Client()
def get_help():
  words = '**Welcome to Covalent Bot API**\nYou can test Covalent API here.\n\nList Covalent API:\n\n1. **Get Token Balances For Address**\nParameter needed (chain_id, address)\n\n2. **Get Historical Portofolio Value Over Time**\nParameter needed (chain_id, address)\n\n3. **Get Transactions**\nParameter (chain_id, address)\n\n4. **Get ERC20 Token Transfer**\nParameter needed (chain_id, address)\n\n'
  return words

@client.event
async def on_ready():
  print('Bot Is Running')

@client.event
async def on_message(message):
  if message.content.startswith('$hello') :
    await message.channel.send('Hello!\noke gan')
  elif message.content.startswith('$help'):
    help = get_help()
    await message.channel.send(help)

client.run(os.getenv('TOKEN'))