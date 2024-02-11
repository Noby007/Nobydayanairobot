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

import threading

from sqlalchemy import Column, String, UnicodeText

from NobyRobot.modules.sql import BASE, SESSION


class ChatLangs(BASE):
    __tablename__ = "chatlangs"
    chat_id = Column(String(14), primary_key=True)
    language = Column(UnicodeText)

    def __init__(self, chat_id, language):
        self.chat_id = str(chat_id)  # ensure string
        self.language = language

    def __repr__(self):
        return "Language {} chat {}".format(self.language, self.chat_id)


CHAT_LANG = {}
LANG_LOCK = threading.RLock()
ChatLangs.__table__.create(checkfirst=True)


def set_lang(chat_id: str, lang: str) -> None:
    with LANG_LOCK:
        curr = SESSION.query(ChatLangs).get(str(chat_id))
        if not curr:
            curr = ChatLangs(str(chat_id), lang)
            SESSION.add(curr)
            SESSION.flush()
        else:
            curr.language = lang

        CHAT_LANG[str(chat_id)] = lang
        SESSION.commit()


def get_chat_lang(chat_id: str) -> str:
    lang = CHAT_LANG.get(str(chat_id))
    if lang is None:
        lang = "en"
    return lang


def __load_chat_language() -> None:
    global CHAT_LANG
    try:
        allchats = SESSION.query(ChatLangs).all()
        CHAT_LANG = {x.chat_id: x.language for x in allchats}
    finally:
        SESSION.close()


__load_chat_language()
