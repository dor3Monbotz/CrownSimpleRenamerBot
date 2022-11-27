import time
import os
from pyrogram import Client, filters, enums
from config import temp, CAPTION, ADMIN
from main.utils import progress_message, humanbytes

@Client.on_message(filters.private & filters.command("rename") & filters.user(ADMIN))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    if len(msg.command) < 2 or not reply:
       return await msg.reply_text("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴏʀ ᴀᴜᴅɪᴏ ᴡɪᴛʜ ғɪʟᴇɴᴀᴍᴇ + .ᴇxᴛᴇɴsɪᴏɴ ᴇx :-(`.mkv` or `.mp4` or `.zip`)")
    media = reply.document or reply.audio or reply.video
    if not media:
       await msg.reply_text("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴏʀ ᴀᴜᴅɪᴏ ᴡɪᴛʜ ғɪʟᴇɴᴀᴍᴇ + .ᴇxᴛᴇɴsɪᴏɴ ᴇx :-(`.mkv` or `.mp4` or `.zip`)")
    og_media = getattr(reply, reply.media.value)
    new_name = msg.text.split(" ", 1)[1]
    sts = await msg.reply_text("ᴛʀʏɪɴɢ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ.....🖤🔥")
    c_time = time.time()
    downloaded = await reply.download(file_name=new_name, progress=progress_message, progress_args=("ᴅᴏᴡɴʟᴏᴀᴅ sᴛᴀʀᴛᴇᴅ.....🥳", sts, c_time)) 
    filesize = humanbytes(og_media.file_size)                
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:            
            await sts.edit(text=f"ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ᴇʀʀᴏʀ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴋᴇʏᴡᴏʀᴅ ●> ({e})")
            return
    else:
        cap = f"{new_name}\n\n💽 sɪᴢᴇ : {filesize}"
    raw_thumbnail = temp.THUMBNAIL 
    if raw_thumbnail:
        og_thumbnail = await bot.download_media(raw_thumbnail)
    else:
        og_thumbnail = await bot.download_media(og_media.thumbs[0].file_id)
    await sts.edit("ᴛʀʏɪɴɢ ᴛᴏ ᴜᴘʟᴏᴀᴅɪɴɢ")
    c_time = time.time()
    try:
        await bot.send_document(msg.chat.id, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("ᴜᴘʟᴏᴀᴅᴇ sᴛᴀʀᴛᴇᴅ.....🥳", sts, c_time))        
    except Exception as e:  
        await sts.edit(f"ᴇʀʀᴏʀ 💔{e}") 
        return               
    try:
        os.remove(downloaded)
        os.remove(og_thumbnail)
    except:
        pass
    await sts.delete()
