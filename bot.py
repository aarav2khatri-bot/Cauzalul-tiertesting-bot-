import discord
import os
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is Online! Logged in as {bot.user}")

# Keep Alive
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running 24/7"

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.run(os.getenv("TOKEN"))
