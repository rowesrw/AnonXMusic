
import asyncio
from strings.filters import command
from AnonXMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER_ID

@app.on_message(filters.command("نادي المطور", [".", ""]) & filters.group)
async def call_dev(client: Client, message: Message):
    chat = message.chat.id
    gti = message.chat.title
    link = await app.export_chat_invite_link(chat)
    usr = await client.get_users(message.from_user.id)
    chatusername = f"@{message.chat.username}"
    user_id = message.from_user.id
    user_ab = message.from_user.username
    user_name = message.from_user.first_name
    buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await app.send_message(OWNER_ID, f"- قام {message.from_user.mention}\n"
                                     f"- بمناداتك عزيزي المطور\n"
                                     f"- الأيدي {user_id}\n"
                                     f"- اليوزر @{user_ab}\n"
                                     f"- ايدي المجموعة {message.chat.id}\n"
                                     f"- الرابط {chatusername}",
                                     reply_markup=reply_markup)

    # إنشاء زر "اونلاين"
    user = await client.get_chat("R7_OX")
    name = user.first_name
    photo = await app.download_media(user.photo.big_file_id)
    online_button = InlineKeyboardButton("{name}", url=f"https://t.me/{user.username}")
    
    await message.reply_photo(photo, caption =f" {name} -› @{user.username} .",
                             disable_web_page_preview=True,
                             reply_markup=InlineKeyboardMarkup([[online_button]]))
