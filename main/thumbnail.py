from pyrogram import Client, filters 
from config import ADMIN, temp

@Client.on_message(filters.private & filters.command("set") & filters.user(ADMIN))                            
async def set_tumb(bot, msg):
    replied = msg.reply_to_message
    if not replied:
        await msg.reply("ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ")
        return
    if not msg.reply_to_message.photo:
       await msg.reply("🤦‍♂ᴏᴏᴘs !! ᴛʜɪs ɪs ɴᴏᴛ ᴀ ᴘʜᴏᴛᴏ")
       return
    Tumb = msg.reply_to_message.photo.file_id
    temp.THUMBNAIL = Tumb
    return await msg.reply(f"ᴛᴇᴍᴘᴏʀᴀʀʏ ᴛʜᴜᴍʙɴᴀɪʟ sᴀᴠᴇᴅ🥳✅️ \nᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ. \n\n`{Tumb}` \n\n👆👆 ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴛʜɪs ɪᴅ ᴛᴏ ʏᴏᴜʀ sᴇʀᴠᴇʀ ᴇɴᴠɪʀᴏ ᴡɪᴛʜ ᴋᴇʏ=`THUMBNAIL`")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    if temp.THUMBNAIL:
        await msg.reply_photo(photo=temp.THUMBNAIL, caption="this is your current thumbnail")
    else:
        await msg.reply_text(text="sᴏʀʀʏ ʏᴏᴜ  ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴛʜᴜᴍʙɴᴀɪʟ💔")
