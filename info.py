import re
from os import environ
from Script import script 
from time import time


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

#rename
FLOOD = int(environ.get("FLOOD", "10"))
RENAME_MODE = bool(environ.get("RENAME_MODE"))

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://te.legra.ph/file/26e43e68d3cd6536b0603.jpg https://te.legra.ph/file/7a2642bc6f0a0b987eb8e.jpg https://te.legra.ph/file/20a8c2563bec0b9d92f35.jpg https://te.legra.ph/file/d150a25376b74ae604218.jpg https://te.legra.ph/file/839c4b37341d83a8c75ad.jpg https://te.legra.ph/file/1c2a4d97d2a78296b2110.jpg https://te.legra.ph/file/add084ad0a9bd117d40f0.jpg https://te.legra.ph/file/1b20ce7ed6e6d26404fd1.jpg https://te.legra.ph/file/8d04fe97aeb9018cf7b66.jpg https://te.legra.ph/file/fc960203396e0f8e084fa.jpg https://te.legra.ph/file/a8625f0dc3857d3cdda50.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/b856bcc3281a959e80b0e.jpg")
NEWGRP = environ.get("NEWGRP", "https://te.legra.ph/file/26e43e68d3cd6536b0603.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/91bd6cd35cb853bef9baa.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/797fdd9725eb981fa087a.jpg")
SP = (environ.get('SP', '')).split()



# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]


auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
login_channel = environ.get('LOGIN_CHANNEL')
LOGIN_CHANNEL = int(login_channel) if login_channel and id_pattern.search(login_channel) else None


# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Tommy")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Custom Chats
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', ''))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', '')

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

#shortlink
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'onepagelink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c075b483992784084270b6365b00fce87c4a13ab')


# Others
VERIFY = bool(environ.get('VERIFY', False))
#SHORTLINK_URL = environ.get('SHORTLINK_URL', 'onepagelink.in')
#SHORTLINK_API = environ.get('SHORTLINK_API', 'c075b483992784084270b6365b00fce87c4a13ab')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/GM_MOVIE_REQUEST')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/GeethaMovies')
MSG_ALRT = environ.get('MSG_ALRT', 'Piracy Is Crime')
NOR_ALRT =  environ.get('NOR_ALRT', 'NO IMAGES IS FOUND')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Gm_Support_Group')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
CUSTOM_QUERY_CAPTION = environ.get("CUSTOM_QUERY_CAPTION", f"{script.CUSTOM_QUERY_CAPTION}")
CAPTION = environ.get("CAPTION", f"{script.CAPTION}")
BR_IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.BR_TEMPLATE_TXT}")
BATCH_LINK = environ.get('BATCH_LINK',"")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#redict
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/GeethaMovies")
FILE_FORWARD = environ.get('FILE_FORWARD',"")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))

LANGUAGES = ["MALAYALAM", "TAMIL", "ENGLISH", "HINDI", "TELUGU", "KANNADA" "DUBBED"]

# Delete Time
IMDB_DLT_TIME = int(environ.get('IMDB_DLT_TIME', 600))

# heroku
HRK_APP_NAME = environ.get('HRK_APP_NAME', 'mybots')
HRK_API = environ.get('HRK_API', '0')



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
