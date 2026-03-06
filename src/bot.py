import os
import asyncio
import discord
from discord.ext import tasks
from dotenv import load_dotenv
from scraper import PriceScraper
from database import init_db, log_price, get_lowest_price

load_dotenv() # Loads tokens from .env file

# --- CONFIGURATION ---
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
PRODUCT_URL = "INSERT_YOUR_URL_HERE"
SELECTOR = "INSERT_CSS_SELECTOR_HERE" # e.g., ".a-price-whole"
TARGET_PRICE = 500.0
PRODUCT_NAME = "My Item"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@tasks.loop(hours=6)
async def check_price():
    channel = client.get_channel(CHANNEL_ID)
    if not channel: return

    scraper = PriceScraper()
    current_price = await scraper.fetch_price(PRODUCT_URL, SELECTOR)
    
    if current_price:
        all_time_low = get_lowest_price(PRODUCT_NAME)
        
        if current_price < all_time_low:
            msg = f"🔥 **NEW ALL-TIME LOW!**\n{PRODUCT_NAME} is now **${current_price}** (Previous low: ${all_time_low})\n{PRODUCT_URL}"
        elif current_price <= TARGET_PRICE:
            msg = f"✅ **Price Alert!**\n{PRODUCT_NAME} is **${current_price}**\n{PRODUCT_URL}"
        else:
            msg = None # No alert needed

        if msg: await channel.send(msg)
        
        log_price(PRODUCT_NAME, current_price)
        print(f"Logged {PRODUCT_NAME} at ${current_price}")

@client.event
async def on_ready():
    print(f'Bot active as {client.user}')
    init_db()
    check_price.start()

if __name__ == "__main__":
    client.run(TOKEN)