from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hai! aku bot musik untuk di obrolan grub ⛓.

Berikut Adalah Commandnyaa:

/play - play reply musik file atau link youtube
/pause - pause menjeda musik
/resume - resume memulai kembali
/skip - skip untuk melanjutkan lagu berikutnya
/stop - clear muntuk berhentikan musik
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/caritemanataudoi"
                    ),
                    InlineKeyboardButton(
                        "⛓ Owner", url="https://t.me/aestheticboyy2"
                    )
                ]
            ]
        )
    )
