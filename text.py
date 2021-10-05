from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

#class Text(object):
START = """"**Hai👋 {} ,
A Simple PDsik Uploader Bot. It Can Upload Link To PDisk.
Send Me Any Direct Link Or YouTube or Video Link I Will Upload To PDisk And Give Direct Pdisk Link
/help for More detail
Made With❤BY @MyTestBotZ**
"""

HELP = """**How to Use Me...
⦿ Its Easy to Use me {} **
✪ » Send me Any Direct Link or YouTube Link
✪ »i will upload to PDisk & Give Link
➠ **If you want Upload Telegram file,Videos to PDisk**
✪ » First Send any File to <a href="https://telegram.me/Link4filesbot">@Link4Filesbot</a> to generate Direct Link
✪ » Copy Generated Link and Paste here...
✪ » Violaaaa.... Done 🥳🥳🥳🥳
"""

ABOUT = """➠ **My Name : PDisk Upload bot**
➠ **Creator : <a href="https://telegram.dog/oo7robot">This Person</a>**
➠ Credits : <code>Everyone in this journey</code>
➠ Language : <code>Python3.9.6</code>
➠ Library : <a href="https://docs.pyrogram.org/">Pyrogram v1.2.9</a>
➠ Cloned From : <b>Paritosh Kumar</b> Source code
➠ Source Code : 
➠ Server : <b>Heroku</b>
➠ Build Status : <b>Stable V1</b>
"""

SB = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⭕️ Updates Channel ⭕️", url="https://t.me/MyTestBotZ")
      ],[
        InlineKeyboardButton("👨‍💻 Creator", url="https://t.me/OO7ROBOT"),
        InlineKeyboardButton("🍿 OtherBots", url="https://telegram.me/mybotzlist")
     ]]
    )

 
@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply_text(
        text=START.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=SB,
        reply_to_message_id=message.message_id
    )

@bot.on_message(filters.command('help') & filters.private)
async def help(bot, message):
    await message.reply_text(
        text=HELP.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=SB,
        reply_to_message_id=message.message_id
    )
 
@bot.on_message(filters.command('about') & filters.private)
async def about(bot, message):
    await message.reply_text(
        text=ABOUT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=SB,
        reply_to_message_id=message.message_id
    )
