import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix = 'Bot') # 呼叫機器人 Bot 的命令字首

@Bot.event
async def on_ready():
    print(">>Bot is Online<<")

Bot.run('') # 啟動