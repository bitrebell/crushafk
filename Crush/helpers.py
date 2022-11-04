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

from typing import Union
from datetime import datetime, timedelta
from Crush import cleanmode, app, botname
from Crush.database import is_cleanmode_on
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=5),
    }
    cleanmode[chat_id].append(put)


async def auto_clean():
    while not await asyncio.sleep(30):
        try:
            for chat_id in cleanmode:
                if not await is_cleanmode_on(chat_id):
                    continue
                for x in cleanmode[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(chat_id, x["msg_id"])
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            continue
                    else:
                        continue
        except:
            continue


asyncio.create_task(auto_clean())


RANDOM = [
    "https://te.legra.ph/file/726926b642c34831ea787.jpg"
    "https://te.legra.ph/file/945b6fd999a4774d9e8f5.jpg"
    "https://te.legra.ph/file/55525404e91234ab6dda5.jpg"
    "https://te.legra.ph/file/cef41d4ec3e0bb822e98c.jpg"
    "https://te.legra.ph/file/8cec6df3f12328d3bd3bf.jpg"
    "https://te.legra.ph/file/f58a778b4dd5451c7f4cc.jpg"
    "https://te.legra.ph/file/6465ee4a422093c2208e6.jpg"
    "https://te.legra.ph/file/f4259552c1a85cab0edf8.jpg"
    "https://te.legra.ph/file/4c09105659848dd51a1be.jpg"
    "https://te.legra.ph/file/689d7577c3c478d7a4ef4.jpg"
    "https://te.legra.ph/file/e4ee341d973bc6ece2374.jpg"
    "https://te.legra.ph/file/97173c58396675272802b.jpg"
    "https://te.legra.ph/file/441ad92db4fa010f3db36.jpg"
]


HELP_TEXT = f"""Welcome to {botname}'s Help Section.

- When someone mentions you in a chat, the user will be notified you are AFK. You can even provide a reason for going AFK, which will be provided to the user as well.


/afk - This will set you offline.

/afk [Reason] - This will set you offline with a reason.

/afk [Replied to a Sticker/Photo] - This will set you offline with an image or sticker.

/afk [Replied to a Sticker/Photo] [Reason] - This will set you afk with an image and reason both.


/settings - To change or edit basic settings of AFK Bot.

For Any Help :- @crushbot_support
"""

def settings_markup(status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="🔄 Clean Mode", callback_data="cleanmode_answer"),
            InlineKeyboardButton(
                text="✅ Enabled" if status == True else "❌ Disabled",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text="🗑 Close Menu", callback_data="close"),
        ],
    ]
    return buttons
