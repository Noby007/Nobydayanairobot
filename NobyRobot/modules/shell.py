 
Copyright (C) 2017-2019, Paul Larsen
<<<<<<< HEAD
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Noby007/NobyRobot-3 ]
=======
.

import subprocess

from telegram import ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler

from NobyRobot import LOGGER, NEKO_PTB
from NobyRobot.modules.helper_funcs.chat_status import dev_plus


@dev_plus
def shell(update: Update, context: CallbackContext):
    message = update.effective_message
    cmd = message.text.split(" ", 1)
    if len(cmd) == 1:
        message.reply_text("No command to execute was given.")
        return
    cmd = cmd[1]
    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    stdout, stderr = process.communicate()
    reply = ""
    stderr = stderr.decode()
    stdout = stdout.decode()
    if stdout:
        reply += f"*Stdout*\n`{stdout}`\n"
        LOGGER.info(f"Shell - {cmd} - {stdout}")
    if stderr:
        reply += f"*Stderr*\n`{stderr}`\n"
        LOGGER.error(f"Shell - {cmd} - {stderr}")
    if len(reply) > 3000:
        with open("NobyRobot.txt", "w") as file:
            file.write(reply)
        with open("NobyRobot.txt", "rb") as doc:
            context.bot.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id,
            )
    else:
        message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


SHELL_HANDLER = CommandHandler(["sh"], shell, run_async=True)
NEKO_PTB.add_handler(SHELL_HANDLER)
__mod_name__ = "Shell"
__command_list__ = ["sh"]
__handlers__ = [SHELL_HANDLER]
