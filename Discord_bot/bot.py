import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix = 'Bot') # 呼叫機器人 Bot 的命令字首

@Bot.event
async def on_ready():
    print(">>Bot is Online<<")

Bot.run('OTI3MzgwNjU5ODMwNDA3MTk4.YdJYiw.N-CRLRdmrJBbQ7ZiR4tZzMd8c1U') # 啟動