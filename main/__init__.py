from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "21740783")
API_HASH = config("API_HASH", "a5dc7fec8302615f5b441ec5e238cd46")
BOT_TOKEN = config("BOT_TOKEN", "7116266807:AAFiuS4MxcubBiHRyzKEDnmYPCRiS0f3aGU")
BOT_UN = config("BOT_UN", default=None)
AUTH_USERS = config("AUTH_USERS", "6299192020")
LOG_CHANNEL = config("LOG_CHANNEL", default=None)
LOG_ID = config("LOG_ID", default=None)
FORCESUB = config("FORCESUB", default=None)
FORCESUB_UN = config("FORCESUB_UN", default=None)
ACCESS_CHANNEL = config("ACCESS_CHANNEL", default=None)
MONGODB_URI = config("MONGODB_URI", "mongodb+srv://Speedwolf1:speedwolf24689@cluster0.rgfywsf.mongodb.net/")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
