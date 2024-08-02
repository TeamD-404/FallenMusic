from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = getenv("DURATION_LIMIT", "90")

OWNER_ID = getenv("OWNER_ID")

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8386a5aa07dddcf5bb185.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/7b053a55193351974f7f1.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+a15zDRlpRlMyOWJl")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/royal_dp_tg")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6454209118").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
