#
# Copyright (C) 2022-2023 by @bitrebell, < https://github.com/birebell >.
#
# This file is part of < https://github.com/bitrebell/crushafk > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Darkranger00/bitrebell/tree/main/LICENSE >
#
# All rights reserved.
#

from Crush import db

usersdb = db.users


async def is_afk(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False, {}
    return True, user["reason"]


async def add_afk(user_id: int, mode):
    await usersdb.update_one(
        {"user_id": user_id}, {"$set": {"reason": mode}}, upsert=True
    )


async def remove_afk(user_id: int):
    user = await usersdb.find_one({"user_id": user_id})
    if user:
        return await usersdb.delete_one({"user_id": user_id})


async def get_afk_users() -> list:
    users = usersdb.find({"user_id": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list
