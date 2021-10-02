from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, 𝐈'𝐀𝐌 𝐀𝐥𝐢𝐳𝐚 𝐌𝐮𝐬𝐢𝐜 🐬|•.•|  {bn} 🎵

𝐈 𝐂𝐚𝐧 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐒𝐞𝐱𝐲 𝐆𝐫𝐨𝐮𝐩 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭. 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 🤞 [נαηvι](https://t.me/HEENAXD).

𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐏𝐥𝐚𝐲 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐀𝐧𝐝 𝐇𝐢𝐠𝐡 𝐐𝐮𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💝 𝐃𝐞𝐯 ", url="https://t.me/XD_LIF")
                  ],[
                    InlineKeyboardButton(
                        "💕 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/MISTY_SUPORTER"
                    ),
                    InlineKeyboardButton(
                        "✨ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/MISTY_SUPORT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐀𝐥𝐢𝐳𝐚 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐂𝐡𝐚𝐭𝐢𝐧𝐠 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/L0VEXWORLD")
                ]
            ]
        )
   )


