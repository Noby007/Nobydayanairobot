"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
<<<<<<< HEAD
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Noby007/NobyRobot-3 ]
=======
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [https://github.com/Noby007/Nobydayanairobot ]
>>>>>>> e59203a234f3c8d397340ee39d56818beb5ff624
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from telethon import Button

from NobyRobot import tbot
from NobyRobot.events import register

PHOTO = "https://te.legra.ph/file/7a18675abd9b75230735d.mp4"


@register(pattern=("Good morning"))
async def awake(event):
    NEKO = f" Welcome this beautiful morning with a smile on your face. I hope youll have a great day today. Wishing you a very good morning! {event.sender.first_name}"
    BUTTON = [
        [
            Button.url("Meet Me Here🎀", "https://telegram.dog/Besties_XD"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
