class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7202072688"
    sudo_users = "7222795580", "6180999156" , "6055161715"
    GROUP_ID = -1001548130580
    TOKEN = "6811413507:AAGIJ-8b9FLADJtTEvcBdjLBsCQh9FDKItc"
    mongo_url = "mongodb+srv://PhiloWise:Philo@waifu.yl9tohm.mongodb.net/?retryWrites=true&w=majority&appName=Waifu"
    PHOTO_URL = ["https://telegra.ph/file/8d9c4af9b7705b1aafc99.jpg", "https://telegra.ph/file/8d9c4af9b7705b1aafc99.jpg"]
    SUPPORT_CHAT = "PhiloMusicSupport"
    UPDATE_CHAT = "TechPiroBots"
    BOT_USERNAME = "@Husbando_Snatch_Bot"
    CHARA_CHANNEL_ID = "-1002225093492"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
