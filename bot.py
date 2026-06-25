import discord
from discord import ui, app_commands, SelectOption
import json
import os
import asyncio
import random
import string
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

CONFIG = {
    "tester_role": None,
    "high_tester_role": None,
    "admin_role": None,
    "staff_role": None,
    "helper_role": None,
    "gamemode_channels": {}
}

# ====================== BASIC COMMANDS ======================
@tree.command(name="ping", description="Check if bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Bot is Online!")

@tree.command(name="setup_role", description="Setup roles")
async def setup_role(interaction: discord.Interaction, tester: discord.Role, high_tester: discord.Role, admin: discord.Role, staff: discord.Role, helper: discord.Role):
    CONFIG["tester_role"] = tester.id
    CONFIG["high_tester_role"] = high_tester.id
    CONFIG["admin_role"] = admin.id
    CONFIG["staff_role"] = staff.id
    CONFIG["helper_role"] = helper.id
    await interaction.response.send_message("✅ Roles Saved!", ephemeral=True)

# ====================== TICKET PANEL ======================
@tree.command(name="panel", description="Create panel")
@app_commands.choices(panel_type=[
    app_commands.Choice(name="tickets", value="tickets")
])
async def panel_cmd(interaction: discord.Interaction, panel_type: str, channel: discord.TextChannel):
    embed = discord.Embed(title="🎟️ Ticket System", description="Select the appropriate ticket type below.\n\n🤝 Partnership\n❓ Support\n🚨 Staff Abuse\n🎁 Redeem Rewards\n📢 Advertisement\n⚖️ Appeal", color=0x00FFFF)
    await channel.send(embed=embed)
    await interaction.response.send_message("✅ Ticket Panel Created!", ephemeral=True)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ {bot.user} is Online and Ready!")

# ====================== KEEP ALIVE ======================
app = Flask('')

@app.route('/')
def home():
    return "Bot is Running 24/7 on Railway"

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.run(os.getenv("TOKEN"))
