class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6706599079"
    sudo_users = "5985087699", "6706599079"
    GROUP_ID = -4255869532
    TOKEN = "7280839062:AAHtqdPU3wWIm_nYTyrVpVuS07___yq8zyU"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "nexus_supp1"
    UPDATE_CHAT = "nexus_supp2"
    BOT_USERNAME = "nexus_girlS_catcher_bot"
    CHARA_CHANNEL_ID = "-4255869532"
    api_id = 28767193
    api_hash = "b8992408188626f6a64edc1579323a14"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
