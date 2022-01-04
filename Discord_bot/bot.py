# 解決 from import 例外處理
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)

import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

# discord.py 1.5 版本更新 訂閱所有事情
intents = discord.Intents.all()

Bot = commands.Bot(command_prefix = 'Bot ', intents = intents) # 呼叫機器人 Bot 的命令字首

@Bot.event # 事件
async def on_ready(): # 判斷機器人是否連線
    print(">>Bot is Online<<")

@Bot.command()
async def load(ctx, extension):
    Bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@Bot.command()
async def unload(ctx, extension):
    Bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@Bot.command()
async def reload(ctx, extension):
    Bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')


for filename in os.listdir('./cmds'): # 列出資料夾內所有的文件
    if filename.endswith('.py'): # 結尾是.py
        Bot.load_extension(f'cmds.{filename[:-3]}') # :-3 不要印出.py

if __name__ == "__main__": 
    Bot.run(jdata['TOKEN']) # 啟動