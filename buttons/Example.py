import discord


class ExampleButton(discord.ui.View):
    @discord.ui.button(label="Press Me!", style=discord.ButtonStyle.green)
    async def example_button(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        print("Working")
        await interaction.response.send_message("I work!")
