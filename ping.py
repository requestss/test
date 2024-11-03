import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'MTMwMjY4NTgwMDQ2NjQ4NTI4OA.Gk3bcY.XWZWiuB0JJz3NpangCBvRdnbVCwu_GfKdUSOuo'

# Set up bot with a command prefix
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix='>', intents=intents)

# Set the target user ID here
TARGET_USER_ID = 961667454210277386  # Replace this with the actual user ID

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Check if the message mentions the target user ID
    if message.mentions:
        for user in message.mentions:
            if user.id == TARGET_USER_ID:
                # Create an embed
                embed = discord.Embed(
                    title="hold this mute",
                    description=f"{message.author.mention}'s dumbass mentioned beta",
                    color=discord.Color.blue()
                )
                # Add a GIF (you can replace the URL with any valid GIF link)
                embed.set_image(url="https://tenor.com/view/central-cee-gif-25355253")
                await message.channel.send(embed=embed)
                break  # Exit after sending the embed to avoid multiple sends

    # Process commands if any
    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)
