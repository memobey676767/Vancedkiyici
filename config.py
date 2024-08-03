import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv(22659994))
API_HASH = getenv("2c89964a0088a7a39ec819c60ae67de7")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("5909970619:AAEy3x02B8eyKN5ndhrYzlGqRf37K_ND0zg")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://acha:acha@cluster0.pjq3j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 360))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001343199487"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6563936773))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Rq7mg/Vancedkiyici",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kycmusicdestek")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kiyicitayfaa")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFZw5oAgewWLrNY04sek0zw_KOu7oSYv20zzf1pzP2A12BMqIAUFj-HupbN6N90Z4pjtIWJ9kNBjMkewWOS6Xt3MFKhdto1iOAwru258wWqCPajF5Zgb0qXAsWgH1tfUjm3eqa7FI5qLFe-aTo8CDiN3ww8IKMbW6HeRPAn7II_7qrwo1DaUlA6bx943BkA7FNWhd_lVXMkOQ27UfK-uMj-o3Djnx2vngAVlEmxHqn6RCYSppsc89xcwlT2nL8alTNZ8qowVsjlIm1HGtuq_3CjhXXuPBEuGHG-VljGTwb9D3pWGQ6IL-500m4_reH3PJN2NYjYtrFNzDTsqTVmuxSA4ATJRQAAAAG-dXUpAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/Panda-06-24-7"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Panda-06-24-7")
PLAYLIST_IMG_URL = "https://telegra.ph/Panda-06-24-7"
STATS_IMG_URL = "https://telegra.ph/Panda-06-24-7"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Panda-06-24-7"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Panda-06-24-7"
STREAM_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Panda-06-24-7"
YOUTUBE_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Panda-06-24-7"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/Panda-06-24-7"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
