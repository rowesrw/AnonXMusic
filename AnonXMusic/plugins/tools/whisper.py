from AnonXMusic import app as bot
from config import BOT_USERNAME
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton

@bot.callback_query_handler(func=lambda call: True)
def n__(call: types.CallbackQuery):
    data = call.data
    if len(data.split(" ")) == 3:
        packList = data.split(" ")
        recipient = packList[2]
        NumMsg = int(packList[0])
        typeWh = packList[1]
        sender = call.from_user.username
        dat = get_content_WH_MSG(NumMsg)
        # print(dat)
        if len(dat) and dat[3] == "whisper":
            if sender in [dat[0], dat[1]]:
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    text=f"الهمسة من  {call.from_user.first_name}: { dat[2]}",
                    show_alert=True,
                )
            else:
                bot.answer_callback_query(
                    callback_query_id=call.id,
                    text="هذي مو الك يا بطل ! :(",
                    show_alert=True,
                )


def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(3)


if name == "main":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nExiting by user request.\n")
        sys.exit(0)
