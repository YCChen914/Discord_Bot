import discord
from discord.ext import commands

# 解決 from core.classes import Cog_Extension 例外處理
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)

class Cog_Extension(commands.Cog):
    def __init__(self,Bot):
        self.bot = Bot
