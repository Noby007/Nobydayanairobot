import pyrate_limiter as pl
from telegram import Update
from telegram.ext import CommandHandler, Filters, MessageHandler
import NobyRobot.modules.sql.blacklistusers_sql as sql
from NobyRobot import ALLOW_EXCL, DEMONS, DEV_USERS, DRAGONS, TIGERS, WOLVES

CMD_STARTERS = ("/", "!") if ALLOW_EXCL else ("/",)

class AntiSpam:
    def __init__(self):
        self.whitelist = (DEV_USERS or []) + (DRAGONS or []) + (WOLVES or []) + (DEMONS or []) + (TIGERS or [])
        pl.Duration.CUSTOM = 15
        self.limiter = pl.Limiter(
            pl.RequestRate(6, pl.Duration.CUSTOM),
            pl.RequestRate(20, pl.Duration.MINUTE),
            pl.RequestRate(100, pl.Duration.HOUR),
            pl.RequestRate(1000, pl.Duration.DAY),
            bucket_class=pl.InMemoryBucket,
        )

    def check_user(self, user):
        if user in self.whitelist or self.limiter.try_acquire(user):
            return False
        return True

SpamChecker = AntiSpam()
MessageHandlerChecker = AntiSpam()

class CustomCommandHandler(CommandHandler):
    def __init__(self, command, callback, admin_ok=False, allow_edit=False, **kwargs):
        super().__init__(command, callback, **kwargs)
        if not allow_edit:
            self.filters &= ~(Filters.update.edited_message | Filters.update.edited_channel_post)

    def check_update(self, update):
        if not isinstance(update, Update) or not update.effective_message:
            return
        message = update.effective_message
        user_id = update.effective_user.id if update.effective_user else None
        if user_id and sql.is_user_blacklisted(user_id):
            return False
        if message.text and len(message.text) > 1:
            fst_word = message.text.split(None, 1)[0]
            if len(fst_word) > 1 and any(fst_word.startswith(start) for start in CMD_STARTERS):
                args = message.text.split()[1:]
                command = fst_word[1:].split("@")
                command.append(message.bot.username)
                if user_id == 1087968824:
                    user_id = update.effective_chat.id
                if not (command[0].lower() in self.command and command[1].lower() == message.bot.username.lower()) or SpamChecker.check_user(user_id):
                    return None
                filter_result = self.filters(update)
                if filter_result:
                    return args, filter_result
                return False

