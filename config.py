from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "2010121827:AAEppkPs28jlqZXKZf0de1ElhEdHEFkZdiU")
SESSION_NAME = getenv("SESSION_NAME", "AQCtWtuSSHrM3OZcCekFbVmpY8ZDcl2JPjgUrFMlS5i82uWvNGCHykE_x_SaFI2deO1rAi58wpAQVLFHCbsJMWV_EgIAdVJu51ElYGg95vXXwDSr1a5rpnaxsMS2BXKIF4LeUMvqU1LuptqD3kmBb6hXg8IR0QDHBRjamKI-TPSknVro57Ign8kL5oosiSccVRVSgaoJogEs9e9f35aOzv-i9CwwTmS71uD5RxsJD7nU3i9CFvlAyljP3ws65OUo33IXPo7UJB2O2ndQJ9MxCWcUK8mObNI5tqwU01xm4mKF6SpqoE1ZxkUXoaj8uSTwlYIpbd1ijidEZ63VWQ2rvMB2dv_stgA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Playvideo1BoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rr8r9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
