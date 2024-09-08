#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7332379566:AAHYB0-2ZInV6bVpCNqf44AbwGKKcQd7Rqw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22759022"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "32d849219dff492d2c3632cffa0bfb85")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002164337955"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7400335416"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = "mongodb+srv://sagatobots00001:sagatobots100@cluster00001.vgdshkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster00001"
DB_NAME = os.environ.get("DATABASE_NAME", "Hanabi_Hyuga_Robot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "instantearn.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "0ba70e421f3f5c473c51ecb41c1792428da3a25c")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","The_Hentai_Society")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002037398576"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Kᴏɴɴɪᴄʜɪᴡᴀ!! {mention}⚡\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n𝐇ᴀɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+1ft76E13mrQ4NzM1'>⛩️ ᴛʜᴇ ᴘᴇʀᴠᴇʀᴛ sᴏᴄɪᴇᴛʏ ⛩️</a></b>")
try:
    ADMINS=[6727550037]
    for x in (os.environ.get("ADMINS", "7400335416 7162615398 1683225887").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Kᴏɴɴɪᴄʜɪᴡᴀ {mention}❤️,\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.\n\n𝐇ᴀɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+1ft76E13mrQ4NzM1'>⛩️ ᴛʜᴇ ᴘᴇʀᴠᴇʀᴛ sᴏᴄɪᴇᴛʏ ⛩️</a></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Dᴏɴ'ᴛ sᴇɴᴅ ᴍᴇ ᴍᴇssᴀɢᴇs ᴅɪʀᴇᴄᴛʟʏ I ᴀᴍ ᴏɴʟʏ Wᴏʀᴋ Fᴏʀ @Straw_Hat_Bots..."

ADMINS.append(OWNER_ID)
ADMINS.append(6727550037)

LOG_FILE_NAME = "sanjisamatokenbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
