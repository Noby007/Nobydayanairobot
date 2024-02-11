  

from telethon import Button

from NobyRobot import tbot
from NobyRobot.events import register

PHOTO = "https://telegra.ph/file/70061cba45ee824dad6f6.jpg"


@register(pattern=("/repo"))
async def awake(event):
    NEKO = """
         We Are So Happy To Announce That We Have Public Our NobyRobot Repo. ✨🥀
➖➖➖➖➖➖➖➖➖➖➖➖➖
「@NekoCuteBot」
➖➖➖➖➖➖➖➖➖➖➖➖➖
Here is the Repo Deploy your Own NobyRobot.
<<<<<<< HEAD
⚜️Repo ➤ https://github.com/Noby007/NobyRobot-3.git
=======
⚜️Repo ➤https://github.com/Noby007/Nobydayanairobot.git
>>>>>>> e59203a234f3c8d397340ee39d56818beb5ff624
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰 Thanks for your support 
It's Fully stable Repo so you can deploy and make own Bot.
──────────────────
Powered By:- @Besties_XD
"""

    BUTTON = [
        [
            Button.url("📢 Repository", "https://github.com/Noby007/NobyRobot-3"),
            Button.url("💻 Collaborators", "https://telegra.ph/Neko-X-05-23"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
