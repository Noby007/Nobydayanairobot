"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
<<<<<<< HEAD
Copyright (C) 2022-2023, Awesome-Prince, [ https://github.com/Noby007]
Copyright (c) 2022-2023, Programmer Network, [ https://github.com/Noby007/NobyRobot-3 ]
=======
.

from telethon import events

from NobyRobot import tbot


def register(**args):
    """Registers a new message."""
    pattern = args.get("pattern")

    r_pattern = r"^[/!]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = f"(?i){pattern}"

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        tbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def chataction(**args):
    """Registers chat actions."""

    def decorator(func):
        tbot.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def userupdate(**args):
    """Registers user updates."""

    def decorator(func):
        tbot.add_event_handler(func, events.UserUpdate(**args))
        return func

    return decorator


def inlinequery(**args):
    """Registers inline query."""
    pattern = args.get("pattern")

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = f"(?i){pattern}"

    def decorator(func):
        tbot.add_event_handler(func, events.InlineQuery(**args))
        return func

    return decorator


def callbackquery(**args):
    """Registers inline query."""

    def decorator(func):
        tbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
