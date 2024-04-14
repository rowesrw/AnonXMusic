import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
                
@app.on_message(
    command(["سورس","المطور"])
    & filters.group
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/bac1995241de705f8fc5c.jpg",
        caption=f"""مرحبا بك عزيزي {message.from_user.mention} \nللتحدث مع مطور البوت اضغط علي الازرار بالاسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        ": 𝗥͜𝗼͡𝗪͡𝗲͜𝗦 💸⤸ ᳒", url=f"https://t.me/R7_OX"), 
                 ],[
                    InlineKeyboardButton(
                        ": GrouP .", url=f"https://t.me/R3_QX"),
                ],[
                
                    InlineKeyboardButton(
                        ": ChanneL .", url=f"https://t.me/RQ_SF"),
                ],

            ]

        ),

    )

@app.on_message(
    command(["سيمو","اسلام","عم الكون","Simo","SIMO","eslam","ESLAM","المطور اسلام"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("DaRrKNneSs_1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\n**NamE** : **{name}**\n**UseR** : **@{usr.username}**\n**iD** : `{usr.id}`\n**BiO** : **{usr.bio}**\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

@app.on_message(
    command(["رويس","رويس باشا","روس","RoWeS","ROWES","rowes","Rowes","المطور رويس"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("R7_OX")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\n**NamE** : **{name}**\n**UseR** : **@{usr.username}**\n**iD** : `{usr.id}`\n**BiO** : **{usr.bio}**\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["بوت","اليكسا"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("AIleXaBoT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**Hi My Name iS {MUSIC_BOT_NAME}**\n\n**A Strong Telegram Bot To Play Music & Video iN The Voice Chat.**\n\n**Just Add Me To Your Group And Send** /help .", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Add me to your Group", url=f"https://t.me/A_N_DBOT?startgroup=True"), 
                 ],[
                
                    InlineKeyboardButton(
                        ": ChanneL .", url=f"https://t.me/RQ_SF"),
                ],

            ]

        ),

    )

@app.on_message(
    command(["محمد","جينيص","GENIUS ","Genius"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("gs_y0")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\n**NamE** : **{name}**\n**UseR** : **@{usr.username}**\n**iD** : `{usr.id}`\n**BiO** : **{usr.bio}**\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

@app.on_message(
    command(["رعد","الراعي","محمد عثمان"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("QIIIlIP")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\n**NamE** : **{name}**\n**UseR** : **@{usr.username}**\n**iD** : `{usr.id}`\n**BiO** : **{usr.bio}**\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
