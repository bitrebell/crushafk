#
# Copyright (C) 2022-2023 by @Darkranger00, < https://github.com/Darkranger00 >.
#
# This file is part of < https://github.com/Darkranger00/crushafk > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Darkranger00/crushafk/tree/main/LICENSE >
#
# All rights reserved.
#

from Crush import db

chatsdb = db.chatsdb


async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})
