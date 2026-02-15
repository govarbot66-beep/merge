import os


class Config(object):
    API_HASH = os.environ.get("d6ddeafb0c189d91b8197ad49103e806")
    BOT_TOKEN = os.environ.get("8513883438:AAFpXRpYkU-qXA8C3tify3AH-WDIVtuWCm8")
    TELEGRAM_API = os.environ.get("28408609")
    OWNER = os.environ.get("ind gamer")
    OWNER_USERNAME = os.environ.get("@ind_gamer_1")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("mongodb+srv://teddugovardhan544_db_user:WVjIA96jQ31net0j@cluster0.kwkkleo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1001002599753693")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
