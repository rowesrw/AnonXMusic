import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

@app.on_message(filters.command("تخ", [".", ""]) & filters.group)
async def ihd(client: Client, message: Message):
    url = f"https://telegra.ph/file/2b3f97cdbf166149b79b6.mp4" 
    msg = message.from_user.mention 
    msgg = message.reply_to_message.from_user.mention
    await client.send_animation(message.chat.id,url,caption="≭︰قتل ↫ ⦗ {msg} ⦘\n≭︰الضحيه دا 😢 ↫ ⦗ {msgg} ⦘\nانا لله وانـا اليـه راجعـون 😢😢",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.reply_to_message.from_user.username}")
                ],
            ]
        )
    )
