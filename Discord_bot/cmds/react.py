# 解決 from core.classes import Cog_Extension 例外處理
import os
import sys
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

class React(Cog_Extension):

    @commands.command()
    async def 圖片(self, ctx):
    #   pic = discord.File(jdata['pic']) # 圖片檔案
        random_pic = random.choice(jdata['pic']) # 網路圖片
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

@commands.command()
async def 網路圖片(self, ctx):
    random_pic = random.choice(jdata['url_pic']) # 隨機圖片
    await ctx.send(random_pic)

def setup(Bot):
    Bot.add_cog(React(Bot))