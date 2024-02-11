"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
<<<<<<< HEAD
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Noby007/NobyRobot-3 ]
=======
.

from telethon import Button

from NobyRobot import tbot
from NobyRobot.events import register

PHOTO = "https://te.legra.ph/file/5cdc460a2ed69abcbee60.gif"


@register(pattern=("Welcome"))
async def awake(event):
    NEKO = f" ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ᴋɪɴɢᴅᴏᴍ♡︎ ɪ ʜᴏᴘᴇ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴍᴀɴʏ ғʀɪᴇɴᴅs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ"
    BUTTON = [
        [
            Button.url("Meet Me Here🎀", "https://telegram.dog/Besties_XD"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
