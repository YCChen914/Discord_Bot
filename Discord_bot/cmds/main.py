# 解決 from core.classes import Cog_Extension 例外處理
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension): # 物件導向 繼承類別

    @commands.command()
    async def ping(self, ctx): # 網路延遲 ctx = context (上下文)
        await ctx.send(f'{round(self.bot.latency * 1000)} (毫秒)') # latency 延遲

    @commands.command()
    async def hi(self, ctx): # 打招呼回覆
        await ctx.send('你好呀~~~')
    
    # 注意 value 一定要有值
    @commands.command()
    async def em(self, ctx): # 嵌入訊息 https://cog-creators.github.io/discord-embed-sandbox/
        embed=discord.Embed(title="自由開源軟體", url="https://moodle.thu.edu.tw/", description="一堂非常有意義的課程", color=0x0597d6, timestamp = datetime.datetime.now()) # 不是台灣的時間
        embed.set_author(name="葉子", url="https://github.com/")
        embed.set_thumbnail(url="https://pcstrike.com/wp-content/uploads/2021/09/Best-Discord-Bots.png")
        embed.add_field(name="Discord Bot", value="FY_Bot", inline=True)
        embed.set_footer(text="謝謝觀看")
        await ctx.send(embed=embed)

    @commands.command() # 需要權限
    async def sayd(self, ctx, *, msg): # 訊息複誦 刪除我所說的訊息、複誦我所說的訊息
        await ctx.message.delete() # 將我們所說的刪掉
        await ctx.send(msg) # 送出我們所說的訊息

    @commands.command() # 需要權限
    async def clean(self, ctx, num : int): # 清除訊息
        await ctx.channel.purge(limit=num+1) # 刪除上限 num +1 加我們打的那行指令
    # 可以做跟時間有關的 有滿多變化的~

def setup(Bot):
    Bot.add_cog(Main(Bot))