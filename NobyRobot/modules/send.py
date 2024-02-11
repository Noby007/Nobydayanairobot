"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
<<<<<<< HEAD
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Noby007/NobyRobot-3 ]
=======
.


from NobyRobot import NEKO_PTB
from NobyRobot.modules.disable import DisableAbleCommandHandler
from NobyRobot.modules.helper_funcs.alternate import send_message
from NobyRobot.modules.helper_funcs.chat_status import dev_plus


@dev_plus
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send, run_async=True)
NEKO_PTB.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [ADD_CCHAT_HANDLER]
