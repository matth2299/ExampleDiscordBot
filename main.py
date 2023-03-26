import asyncio
import json
from discord import app_commands
from discord.utils import get
from discord.ext import commands, tasks
import discord
from buttons.Example import *

with open("config.json") as json_file:
    config = json.load(json_file)

guild = discord.Object(id=config["server_id"])


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.initial_extensions = ["cogs.user_commands"]

    async def setup_hook(self) -> None:
        for ext in self.initial_extensions:
            await self.load_extension(ext)

    async def on_ready(self):
        print("Bot Started")
        self.update_status.start()

    @tasks.loop(seconds=60)
    async def update_status(self):
        await bot.change_presence(activity=discord.Game(name="I'm Alive"))


bot = MyBot()


@bot.tree.command()
@app_commands.checks.has_role("Owner")
async def make_text(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World")


@bot.tree.command()
@app_commands.checks.has_role("Owner")
async def example_button(interaction: discord.Interaction):
    await interaction.response.send_message("Button Test", view=ExampleButton)


@bot.command()
@commands.is_owner()
async def sync(ctx):
    await bot.tree.sync(guild=guild)
    await ctx.send("Synced Slash Commands")


async def main():
    async with bot:
        await bot.start(config["TOKEN"])

asyncio.run(main())
