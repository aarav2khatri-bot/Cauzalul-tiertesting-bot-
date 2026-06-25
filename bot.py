import discord
from discord import app_commands
import os
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command(name="ping", description="Test bot")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Bot is Online!")

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ {bot.user} is successfully logged in!")

# ====================== KEEP ALIVE ======================
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running 24/7"

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.run(os.getenv("TOKEN"))
