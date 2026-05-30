import os
from typing import List

API_ID = os.environ.get("API_ID", "11333800")
API_HASH = os.environ.get("API_HASH", "e1b9a48abe756df09de3cc456975b481")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8747842250:AAHRkNR3xVYYwXcHKPjxyi44co434zHEhmw")
ADMIN = int(os.environ.get("ADMIN", "6505906100"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002186397456"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Strange:Strange@cluster0.wpvqktw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "-1002326865341").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "-1002326865341").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
