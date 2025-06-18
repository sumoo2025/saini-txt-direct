#🄸ɴᴅɪᴀɴ ✗ 🅆ᴀʀʀɪᴏʀ
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "12380656"))
API_HASH = environ.get("API_HASH", "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = environ.get("BOT_TOKEN", "8184347743:AAGiHWH3_cgfcDXDomt4VjtDhRfl7khDSQc")
OWNER = int(environ.get("OWNER", "6026885967"))
CREDIT = "🄸ɴᴅɪᴀɴ ✗ 🅆ᴀʀʀɪᴏʀ"
AUTH_USER = os.environ.get('AUTH_USERS', '6026885967').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
