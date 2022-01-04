# 解決 from core.classes import Cog_Extension 例外處理
import os
import sys

from discord import channel
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener() # 事件
    async def on_member_join(self, member): # 判斷是否有人員加入
        channel = self.Bot.get_channel(int[jdata['Bot_message']]) # bot_message 伺服器
        await channel.send(f'{member} 加入了伺服器！') # send 一定要加 await
        print(f'{member} join!')

    @commands.Cog.listener() # 事件
    async def on_member_remove(self, member): # 判斷是否有人員離開
        channel = self.Bot.get_channel(int[jdata['Bot_message']]) # bot_message 伺服器
        await channel.send(f'{member} 離開了伺服器！') # send 一定要加 await
        print(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg): # 觸發輸入訊息
        if msg.content.endswith('apple'): # 判斷結尾訊息
            await msg.channel.send('聽起來很好吃')
        if msg.content == 'apple': # 判斷訊息
            await msg.channel.send('好吃')
        # 注意！無限洗頻
        #if msg.content == 'apple':
        #    await msg.channel.send('apple')
        # 改善方式
        if msg.content == 'peach' and msg.author != self.bot.user: # 不是機器人發送的情況
            await msg.channel.send('peach')
        keyword = ['apple','pie','cake'] # 關鍵字
        if msg.content in keyword:
            await msg.channel.send('都是食物')

def setup(Bot):
    Bot.add_cog(Event(Bot))
