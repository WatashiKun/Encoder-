# i am using redis db. Its quite handy and easy. i used lists for queue. and redis can only store bytes, str, int or float. so i used codecs to encode list[0] in str then stored in db. when using the stored str, i equated it later decoded it back in its original type using 'codecs' module.
import logging
import asyncio 
import time
import pickle # to dumps/loads 
import codecs # to encode/decode basically
#import requests
#import json cuz i dont nedd this fucking module
#import urllib3 as url ahh

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)



from pyrogram import Client
from pyrogram.types import CallbackQuery
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from pyrogram.errors import FloodWait
from datetime import datetime as dt
#from SmartEncoder.Plugins.compress import *
# database 
from SmartEncoder.Database.db import myDB
import SmartEncoder.Plungins.Labour
from SmartEncoder.Plungins.Queue import *
from SmartEncoder.Plungins.list import *
from SmartEncoder.Tools.eval import *
from SmartEncoder.Addons.download import d_l
from SmartEncoder.Addons.executor import bash_exec
from SmartEncoder.Plungins.cb import *
from SmartEncoder.Addons.list_files import l_s
from SmartEncoder.translation import Translation
from SmartEncoder.Tools.progress import *
from config import Config
from pyrogram import filters, Client, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pathlib import Path
mode_for_custom = []
uptime = dt.now()
mode_for_custom.append("off")



async def resume_task():
  if myDB.llen("DBQueue") > 0:
    queue_ = myDB.lindex("DBQueue", 0)
    _queue = pickle.loads(codecs.decode(queue_.encode(), "base64"))
    await add_task(TGBot, _queue)
      
      
async def start_bot():
  await TGBot.start()
  await resume_task()
  await idle()


#if __name__ == "__main__":
    #loop.run_untill_complete(start_bot())
#rename_task.insert(0, "on")
if __name__ == "__main__":
  @TGBot.on_message(filters.incoming & (filters.video | filters.document))
async def wah_1_man(bot, message: Message):
    if mode_for_custom[0] == "off":
        if message.from_user.id not in Config.AUTH_USERS:
            return

        if rename_task[0] == "off":
            query = await message.reply_text("Added this file to queue.\nCompression will start soon.", quote=True)
            a = message  # using 'a' as message is easy
            pickled = codecs.encode(pickle.dumps(a), "base64").decode()
            myDB.rpush("DBQueue", pickled)  # Assuming myDB is the Redis database connection
            if myDB.llen("DBQueue") == 1:
                await query.delete()
                await add_task(bot, message)  # Assuming add_task() is a function to process the task

        else:
            if message.from_user.id not in Config.AUTH_USERS:
                return

            query = await message.reply_text("**Added this file to rename in queue.**", quote=True)
            rename_queue.append(message)  # Assuming rename_queue is a list for renaming tasks
            if len(rename_queue) == 1:
                await query.delete()
                await add_rename(bot, message)  # Assuming add_rename() is a function to process the rename task
 

  @TGBot.on_message(filters.incoming & filters.command("rename_mode", prefixes=["/", "."]))
      async def help_eval_message(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    OUT = "Rename Mode Has Been Enabled."
    await message.reply_text(OUT, quote=True)
    rename_task.insert(0, "on")
    
    
  @TGBot.on_message(filters.incoming & filters.command("eval", prefixes=["/", "."]))
  async def help_eval_message(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    await eval_handler(bot, message)
  
  @TGBot.on_message(filters.command("dl", prefixes=["/", "."]))
      async def start_cmd_handler(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
      return
    await d_l(bot, update)

  @TGBot.on_message(filters.command("ul", prefixes=["/", "."]))
  async def u_l(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    c_time = time.time()
    input_message = message.text.split(" ", maxsplit=1)[1]
    path = Path(input_message)
 # start = datetime.now()
    if not os.path.exists(path):
      await message.reply_text(f"No such file or directory as `{path}` found", quote=True)
      return
    boa = await message.reply_text("**UPLOADING**", quote=True)
    await bot.send_document(
      chat_id=message.chat.id,
      document=path,
      force_document=True,
      #caption="©️ @Animes_Encoded",
      reply_to_message_id=message.message_id,
      progress=progress_for_pyrogram,
      progress_args=(bot, "UPLOADING", boa, c_time)
    )
    await boa.delete()
  
# bash
  @TGBot.on_message(filters.command("bash", prefixes=["/", "."]))
  async def start_cmd_handler(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    await bash_exec(bot, message)

# ls
  @TGBot.on_message(filters.incoming & filters.command("ls", prefixes=["/", "."]))
  async def lost_files(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    await l_s(bot, message)

# disable normal mode
  @TGBot.on_message(filters.command("manual_mode", prefixes=["/", "."]))
  async def hehe(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return 
    await message.reply_text("I will now wont respond to any file! Reply me with /dl and /ul", quote=True)
    mode_for_custom.insert(0, "on")
  
# able normal mode
  @TGBot.on_message(filters.command("normal_mode", prefixes=["/", "."]))
  async def hehe(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return 
    await message.reply_text("I will now respond to any sent file", quote=True)
    mode_for_custom.insert(0, "off")
    rename_task.insert(0, "off")
  

# start
  @TGBot.on_message(filters.command("start", prefixes=["/", "."]))
  async def start_cmd_handler(bot, message):
    await message.reply_text(
      text=Translation.START_TEXT,
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton("📕Channel", url="https://t.me/AniVoid")
          ],
        ],
      ),
      parse_mode="md"
    )

# ping
  @TGBot.on_message(filters.incoming & filters.command(["ping"]))
  async def up(app, message):
    stt = dt.now()
    ed = dt.now()
    v = TimeFormatter(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await message.reply_text(v + "\n" + p)

# restart 
  @TGBot.on_message(filters.command("restart"))
  async def re(bot, message):
    if message.chat.id in Config.AUTH_USERS:
      await message.reply_text("•Restarting")
      quit(1)
  
# to change ffmpeg variables 
  @TGBot.on_message(filters.command("crf"))
  async def re(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    OUT = f"I will be using : {cr} crf"
    myDB.set('crf', f'{cr}')
    await message.reply_text(OUT, quote=True)

  @TGBot.on_message(filters.command("quality"))
  async def re(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    OUT = f"I will be using : {cr} quality."
    myDB.set('quality', f'{cr}')
    await message.reply_text(OUT, quote=True)
  
  @TGBot.on_message(filters.command("codec"))
  async def re(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    OUT = f"I will be using : {cr} codec"
    myDB.set('codec', f'{cr}')
    await message.reply_text(OUT, quote=True)
  
  @TGBot.on_message(filters.command("audio"))
  async def re(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    _any = message.text.split(" ", maxsplit=1)[1]
    #OUT = "This feature has been removed.\nLibopus audio codec is replaced by Libfdk_aac.\nIt requires vbr instead of audio bitrates.\nDefault vbr is set to `2`.\nYou don't have to change it."
    #myDB.set('audio', f'{cr}')
    audio_.insert(0, f"{_any}")
    await message.reply_text(f"Fine! Your files are {_any} audio 👀", quote=True)
  
  @TGBot.on_message(filters.command("resolution"))
  async def re(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    #OUT = f"I have changed my gear to {cr}"
    #myDB.set('speed', f'{cr}')
    OUT = f"<b>I will use {cr} quality in renaming files<b>"
    quality_.insert(0, f"{cr}")
    await message.reply_text(OUT, quote=True)
  
  
  @TGBot.on_message(filters.command("preset"))
  async def re(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    #OUT = f"I have changed my gear to {cr}"
    #myDB.set('speed', f'{cr}')
    OUT = f"I will use {cr} preset in encoding files."
    myDB.set("speed", f"{cr}")
    await message.reply_text(OUT, quote=True)
  
# audio_mode ( for libopus and libfdk_aac support )

  @TGBot.on_message(filters.command("audio_codec"))
  async def re_codec_(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    #OUT = f"I have changed my gear to {cr}"
    #myDB.set('speed', f'{cr}')
    OUT = f"<b>I will use {cr} audio codec in encoding files.<b>"
    #quality_.insert(0, f"{cr}")
    myDB.set("Audio_Codec", f"{cr}")
    await message.reply_text(OUT, quote=True)
    
# watermark positio
  @TGBot.on_message(filters.command("watermark_position"))
  async def re_w_(bot, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    #OUT = f"I have changed my gear to {cr}"
    #myDB.set('speed', f'{cr}')
    OUT = f"<b>I have set watermark postion to top {cr} corner.<b>"
    #quality_.insert(0, f"{cr}")
    myDB.set("w_p", f"{cr}")
    if myDB.get("w_p") == "Left" or "left":
      myDB.set("w_po","10")
    elif myDB.get("w_p") == "Right" or "right":
      myDB.set("w_po", "w-tw-10")
    await message.reply_text(OUT, quote=True)
# settings
# settings
  @TGBot.on_message(filters.incoming & filters.command(["settings"]))
  async def settings(app, message):
    if message.from_user.id in Config.AUTH_USERS:
      await message.reply_text(
        f"🏷 **Video** \n┏━━━━━━━━━━━━━━━━━\n┣ Codec  ➜ ```{myDB.get('codec')}```\n┣ **Crf**  ➜ ```{myDB.get('crf')}``` \n┣ **Resolution**  ➜ ```{myDB.get('quality')}```\n┗━━━━━━━━━━━━━━━━━\n\n🏷  **Audio** \n┏━━━━━━━━━━━━━━━━━\n┣ **Codec**  ➜ ```{myDB.get('Audio_Codec')}```\n┣  **Bitrates** ➜ ```40k```\n┗━━━━━━━━━━━━━━━━━\n\n🏷 **Watermark**\n┏━━━━━━━━━━━━━━━━━\n┣ **Position** ➜ ```{myDB.get('w_p')}```\n┣ **Size**  ➜ ```{myDB.get('size')}```\n┗━━━━━━━━━━━━━━━━━\n\n🏷 **Speed**\n┏━━━━━━━━━━━━━━━━━\n┣ **Preset** ➜ ```{myDB.get('speed')}```\n┗━━━━━━━━━━━━━━━━━",
        quote=True
      )
      
  @TGBot.on_message(filters.incoming & filters.command(["size"]))
  async def size(app, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    OUT = f"Fine! I have set the watermark text size to `{cr}`"
    await message.reply_text(OUT, quote=True)
    myDB.set("size", f"{cr}")
    
    
  # name
  @TGBot.on_message(filters.incoming & filters.command(["name"]))
  async def settings(app, message):
    if message.from_user.id not in Config.AUTH_USERS:
      return
    cr = message.text.split(" ", maxsplit=1)[1]
    OUT = f"Fine! I have set the name text to be `{cr}`"
    await message.reply_text(OUT, quote=True)
    name.insert(0, f"{cr}")
  # databases
  @TGBot.on_message(filters.incoming & filters.command("clear", prefixes=["/", "."]))
  async def lost_files(bot, message):
    if message.chat.id not in Config.AUTH_USERS:
      return
    myDB.delete("DBQueue")
    await message.reply_text("Successfully cleared queue and removed from database.", quote=True)
  
  cb_bro = CallbackQueryHandler(
    cb_things
  )
  TGBot.add_handler(cb_bro)
  asyncio.get_event().run_until_complete(start_bot)
  
