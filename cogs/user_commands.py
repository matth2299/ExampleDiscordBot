import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from buttons.Example import *
import json

with open("config.json") as json_file:
    config = json.load(json_file)

guild = discord.Object(id=config["server_id"])


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hi", description="Example Command")
    @app_commands.checks.has_role("test")
    async def hi(self, interaction: discord.Interaction):
        print("Hello")
        await interaction.response.send_message("Hello World", view=ExampleButton())


async def setup(bot: commands.Bot):
    await bot.add_cog(UserCommands(bot), guild=discord.Object(id=config["server_id"]))
