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

PHOTO = "https://te.legra.ph/file/4e959d8f074bef7061463.mp4"


@register(pattern=("Good night"))
async def awake(event):
    NEKO = f"Good night I hope tomorrow is the best day in your life. {event.sender.first_name}"
    BUTTON = [
        [
            Button.url("Meet Me Here🎀", "https://telegram.dog/Besties_XD"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
