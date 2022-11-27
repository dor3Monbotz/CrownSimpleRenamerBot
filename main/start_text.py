from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="ᴛʜɪs ɪs ᴘᴇʀsᴏɴᴀʟ ᴜsᴇ ʙᴏᴛ 🙏. ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ? 👇 ᴄʟɪᴄᴋ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴛᴏ ᴅᴇᴘʟᴏʏ"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SOURCE CODE", url="https://github.com/dor3Monbotz/CrownSimpleRenamerBot")
        ],[
        InlineKeyboardButton("🖥️ How To Deploy (ask to owner)", url="https://t.me/little_little_hackur")
    ]])
    if msg.from_user.id != ADMIN:
        await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
        return
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"🙏ɴᴀᴍᴀsᴛᴇ🙏 {msg.from_user.mention} ɪ ᴀᴍ sɪᴍᴘʟᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀsᴏɴᴀʟ ᴜsᴇs.\nᴛʜɪs ʙᴏᴛ ɪs ᴍᴀᴅᴇ ʙʏ <b><a href=https://github.com/dor3Monbotz</a></b>"                                     
    button= [[
        InlineKeyboardButton("🤖 Bot Updates", url="https://t.me/projectcrown")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=f"ᴊᴜsᴛ sᴇɴᴅ ᴀ ғɪʟᴇ ᴀɴᴅ /rename <new name> ᴡɪᴛʜ ʀᴇᴘʟᴀʏᴇᴅ ʏᴏᴜʀ ғɪʟᴇ\n\nʀᴇᴘʟʏ ᴀ ᴘʜᴏᴛᴏ ᴀɴᴅ sᴇɴᴅ /set ᴛᴏ sᴇᴛ ᴛᴇᴍᴘᴏʀᴀʀʏ ᴛʜᴜᴍʙɴᴀɪʟ\n/view ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/little_little_hackur>ᴋᴜɴᴀʟ ɢᴀɪᴋᴡᴀᴅ</a> & <a href=https://t.me/projectcrown>ᴘʀᴏᴊᴇᴄᴛ ᴄʀᴏᴡɴ</a>"  
    Source="<a href=https://github.com/dor3Monbotz/CrownSimpleRenamerBot>Click Here</a>"
    txt=f"<b>ʙᴏᴛ ɴᴀᴍᴇ: {me.mention}\n ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/little_little_hackur</a>\nʙᴏᴛ ᴜᴘᴅᴀᴛᴇs: <a href=https://t.me/projectcrown>ᴄʀᴏᴡɴ ʙᴏᴛᴢ</a>\nMy ᴍᴀsᴛᴇʀ's: {Master}\nsᴏᴜʀᴄᴇ ᴄᴏᴅᴇ: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


