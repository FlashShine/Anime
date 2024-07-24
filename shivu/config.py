class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7202072688"
    sudo_users = "7222795580", "6180999156", "7202072688"
    GROUP_ID = -1002133191051
    TOKEN = "6862816736:AAEblEAoBtPJI9ql4vjr0Q0fmNNenq5_Y7Q"
    mongo_url = "mongodb+srv://pythoncux:pythoncux@cluster0.tl7krxg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/8d9c4af9b7705b1aafc99.jpg", "https://telegra.ph/file/8d9c4af9b7705b1aafc99.jpg"]
    SUPPORT_CHAT = "PhiloMusicSupport"
    UPDATE_CHAT = "TechPiroBots"
    BOT_USERNAME = "Waifu_Anime_Catch_Bot"
    CHARA_CHANNEL_ID = "-1002140495801"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
