import os

API_ID = API_ID =  24798261

API_HASH = os.environ.get("API_HASH", "fef280037f5759eccc540c6d7a279a14")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8582068316:AAFGRnCgt80M5cvR0jXpiPBbVZPrfb8dY8c")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5349573682))

LOG = -1003621974261,

# UPDATE_GRP = -1002140332321, # bot sat group

# auth_chats = [5219193259,1327415906]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5349573682").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


