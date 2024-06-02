@app.on_message(filters.command("تخ", [".", ""]) & filters.group)
async def ihd(client: Client, message: Message):
    url = f"https://telegra.ph/file/2b3f97cdbf166149b79b6.mp4"
    await client.send_photo(message.chat.id,url,caption="≭︰قتل ↫ ⦗ {message.from_user.mention} ⦘\n≭︰الضحيه دا 😢 ↫ ⦗ {message.reply_to_message.from_user.mention} ⦘\nانا لله وانـا اليـه راجعـون 😢😢",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.reply_to_message.from_user.username}")
                ],
            ]
        )
    )


