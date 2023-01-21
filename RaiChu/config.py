## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCdDLjbdJcEiMsNFyk6T0W-wjLfBfHPS2wPnG5psboGVZfdXup0uOrx2Rn_nLQHjhcZZ3qe9z2oiLq6d0EiTQtHGNfe1_OQlki2wL5AwBOBwyf1hQJWvBv53zfs8Evo_EvuNWY77QxZSMIrH-vzUq0FWmV0sMhlG74KzA_G4ysYoZuObO2CnUQV9fnmxTYJUrUg-M99abEVf0GPiYv68ZtPEA8DAmVGB2g9IsmxKREpDLLESs7VzL1WMKumt0Ynyyd7kEn9fqUpz0AlJUzT-8IetPVPEh_NvjDH7EPTbLTf99nA0tNy4lr_sOSpjrNpKwZROEKm1F8MRz96wtYp85RXAAAAAVGnG2QA")
BOT_TOKEN = getenv("BOT_TOKEN", "5989100103:AAEgrSJBumngRO278Bd0CtkZ1Knv9vyw3bg")
BOT_NAME = getenv("BOT_NAME", "Ketone")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Hallogen")
ALIVE_NAME = getenv("ALIVE_NAME", "Nice")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "KetoneMusics")
BOT_USERNAME = getenv("BOT_USERNAME", "KetoneMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ketone Musics")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "KetoneSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "KetoneBots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5001717969").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
