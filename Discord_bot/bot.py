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
async def 圖片(ctx):
#    pic = discord.File(jdata['pic']) # 圖片檔案
    random_pic = random.choice(jdata['pic']) # 網路圖片
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

@Bot.command()
async def 網路圖片(ctx):
    random_pic = random.choice(jdata['url_pic']) # 隨機圖片
    await ctx.send(random_pic)

@Bot.event # 事件
async def on_member_join(member): # 判斷是否有人員加入
    channel = Bot.get_channel(int[jdata['Bot_message']]) # bot_message 伺服器
    await channel.send(f'{member} 加入了伺服器！') # send 一定要加 await
    print(f'{member} join!')

@Bot.event # 事件
async def on_member_remove(member): # 判斷是否有人員離開
    channel = Bot.get_channel(int[jdata['Bot_message']]) # bot_message 伺服器
    await channel.send(f'{member} 離開了伺服器！') # send 一定要加 await
    print(f'{member} leave!')
@Bot.command()
async def ping(ctx): # 網路延遲 ctx = context (上下文)
    await ctx.send(f'{round(Bot.latency * 1000)} (毫秒)') # latency 延遲

Bot.run(jdata['TOKEN']) # 啟動