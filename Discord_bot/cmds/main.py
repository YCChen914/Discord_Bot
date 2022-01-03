# 解決 from core.classes import Cog_Extension 例外處理
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)

import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension): # 物件導向 繼承類別

    @commands.command()
    async def ping(self, ctx): # 網路延遲 ctx = context (上下文)
        await ctx.send(f'{round(self.bot.latency * 1000)} (毫秒)') # latency 延遲

    @commands.command()
    async def hi(self, ctx): # 打招呼回覆
        await ctx.send('你好呀~~~')
def setup(Bot):
    Bot.add_cog(Main(Bot))