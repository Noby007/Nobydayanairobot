 
Copyright (C) 2017-2019, Paul Larsen
<<<<<<< HEAD
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Noby007/NobyRobot-3 ]
=======
.

import threading

from sqlalchemy import Column, String

from NobyRobot.modules.sql import BASE, SESSION


#   |----------------------------------|
#   |  Test Module by @Awesome-Prince |
#   |        Kang with Credits         |
#   |----------------------------------|
class NSFWChats(BASE):
    __tablename__ = "nsfw_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


NSFWChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_nsfw(chat_id):
    try:
        chat = SESSION.query(NSFWChats).get(str(chat_id))
        if chat:
            return True
        else:
            return False
    finally:
        SESSION.close()


def set_nsfw(chat_id):
    with INSERTION_LOCK:
        nsfwchat = SESSION.query(NSFWChats).get(str(chat_id))
        if not nsfwchat:
            nsfwchat = NSFWChats(str(chat_id))
        SESSION.add(nsfwchat)
        SESSION.commit()


def rem_nsfw(chat_id):
    with INSERTION_LOCK:
        nsfwchat = SESSION.query(NSFWChats).get(str(chat_id))
        if nsfwchat:
            SESSION.delete(nsfwchat)
        SESSION.commit()


def get_all_nsfw_chats():
    try:
        return SESSION.query(NSFWChats.chat_id).all()
    finally:
        SESSION.close()
