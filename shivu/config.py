class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7222795580"
    sudo_users = "7222795580", "6180999156" , "7032905213" , "7177206350"
    GROUP_ID = -1001548130580
    TOKEN = "7579121046:AAErJ-zh2HE8zaJTY5V6B0Nkd1nztbhjb3Y"
    mongo_url = "mongodb+srv://PhiloWise:Philo@waifu.yl9tohm.mongodb.net/?retryWrites=true&w=majority&appName=Waifu"
    PHOTO_URL = ["https://telegra.ph/file/8d9c4af9b7705b1aafc99.jpg", "https://telegra.ph/file/8d9c4af9b7705b1aafc99.jpg"]
    SUPPORT_CHAT = "TechPiroBots"
    UPDATE_CHAT = "TechPiroBots"
    BOT_USERNAME = "@Husbando_Snatch_Bot"
    CHARA_CHANNEL_ID = "-1002225093492"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
