import asyncio

import random

from AnonXMusic import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)

from pyrogram import filters, Client





txt = [


            "هل تعرضت لغدر في حياتك؟",
            
            
            "هل تعرف عيوبك؟",


            "هل أنت مُسامح أم لا تستطيع أن تُسامح؟",


            "إذا قمت بالسفر إلى نُزهة خارج بلدك فمن هو الشخص الذي تُحب أن يُرافقك؟هل تتدخل إذا وجدت شخص يتعرض لحادثة سير أم تتركه وترحل؟",


            "ما هو الشخص الذي لا تستطيع أن ترفض له أي طلب؟",


            "إذا أعجبت بشخصٍ ما، كيف تُظهر له هذا الإعجاب أو ما هي الطريقة التي ستتبعها لتظهر إعجابك به؟",


            "هل ترى نفسك مُتناقضً؟",


            "ما هو الموقف الذي تعرضت فيه إلى الاحراج المُبرح؟",


            "ما هو الموقف الذي جعلك تبكي أمام مجموعة من الناس رغمًا عنك؟",


            "إذا جاء شريك حياتك وطلب الانفصال، فماذا يكون ردك وقته؟",


            "إذا كان والد يعمل بعملٍ فقير هل تقبل به أو تستعر منه؟",


            "ما الذي يجعلك تُصاب بالغضب الشديد؟",


           "هإذا وجدت الشخص الذي أحببتهُ في يومٍ ما يمسك بطفله، هل هذا سيشعرك بالألم؟",


           "علاقتك مع اهلك",


           "ثلاثة أشياء تحبها"


        ]


        


@app.on_message(filters.command(["صراحه","صراحة"], ""))

async def sraha(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
