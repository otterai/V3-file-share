from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import *
from datetime import datetime
from helper_func import get_readable_time, encode, is_admin


@Bot.on_message(filters.command('batch') & filters.private & is_admin)
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
