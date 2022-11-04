#
# Copyright (C) 2022-2023 by @Darkranger00, < https://github.com/Darkranger00 >.
#
# This file is part of < https://github.com/Darkranger00/crushafk > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Darkranger00/crushafk/blob/main/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Database to save your chats and stats...
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "").split())
)  # Input type must be interger
