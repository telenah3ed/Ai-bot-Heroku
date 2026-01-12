import os
import logging
from telethon import TelegramClient, events

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- CONFIGURATION ---
# These will be pulled from Heroku's environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the Client
bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Hi! I am your AI Bot deployed on Heroku. How can I help you today?')

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    if not event.text.startswith('/'):
        await event.respond(f"You said: {event.text}")

print("Bot is running...")
bot.run_until_disconnected()
