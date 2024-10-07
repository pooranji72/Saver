#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=23940130, cast=int)
API_HASH = config("API_HASH", default=4d717a6f888e37b7ebde0ace80cd22c6)
BOT_TOKEN = config("BOT_TOKEN", default=7443034654:AAH83ai22x0R_um_D4zHToFIiCAv8M1q4Co)
SESSION = config("SESSION", default=BQFtTCIAP6lFhRrJrxceGpvYZPb4dBa-v9iSs5FU7suGA1xBpqG3G6UwRnsKFfOvVgg8DJFP_K2GUq_aHOPm7H4FTThkNaTdDraPazNCbNylt-yDS0J-h3-OsW9153FGy4vJZPa0N6ABEBrV9WkgZWD0Kib-XVhzJna8hBOnt32WM_CQdDRNy65n6b-NtXWGRVZ33sTp3t7s0fNfEvsQTYYgQfdPv5NHQvym1R0eF8q-dwtbe9lfqfqWrVIN03EMRznVtd9jufpHb_oy_-EmBZDmfAHzXq_ILjO3xC31toHsuGFtfEx3JcWggyLRwZjcNpMLviU9f-reScfm6QU2bx_sTyhAAAAAE81sz9AA)
FORCESUB = config("FORCESUB", default=yuy1326)
AUTH = config("AUTH", default=-1005315677437, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
