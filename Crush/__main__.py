#
# Copyright (C) 2022-2023 by @Darkranger00, < https://github.com/Darkranger00 >.
#
# This file is part of < https://github.com/Darkranger00/crushafk > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Darkranger00/crushafk/tree/main/LICENSE >
#
# All rights reserved.
#

import asyncio
import importlib

from pyrogram import idle

from Crush.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def initiate_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("Crush.modules." + all_module)
    print("Started Crush AFK Bot.")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
