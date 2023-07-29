import logging
import os
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
import SmartEncoder.Plugins.Labour
from SmartEncoder.Plugins.Queue import *
from SmartEncoder.Plugins.list import *
from SmartEncoder.Tools.eval import *
from SmartEncoder.Addons.download import d_l
from SmartEncoder.Addons.executor import bash_exec
from SmartEncoder.Plugins.cb import *
from SmartEncoder.Addons.list_files import l_s
from SmartEncoder.translation import Translation
from SmartEncoder.Tools.progress import *
from config import Config
from pyrogram import filters, Client, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pathlib import Path



import anitopy
import os

async def anitopy_renamer(query):
  execute = anitopy.parse(query)
  if 'anime_title' in execute:
    title = execute['anime_title']
  else:
    title = 'Episode'    
  if 'episode_number' in execute:
    episode = execute['episode_number']
  else:
    episode = "Episode"
  if 'video_resolution' in execute:   
    resolution = execute['video_resolution']   
  else:
    resolution = '[720p]'
 # if "AnimeKayo" in title:
    #title_ = title.replace("AnimeKayo", "")
  if episode == "Episode":
    bb = title.replace("S01E", "")
    final = f"{bb} [{quality_[0]}] [{audio_[0]}] @AniVoid.mkv"
   #final = f"{len(rename_queue)} - {title} [480p] [Sub] @AniVoid.mkv"
  else:
    if len(audio_) == 0:
      if len(quality_) == 0:
        final = "{} - {}.mkv".format(episode, title)
    else:
#t = title.replace("Anime Time", "")
      #final = f"{episode} - {title} [{quality_[0]}] [{audio_[0]}] @AniVoid.mkv"
      #ee_ = episode.replace("E", "")
      #t_t = title.replace("-", " ")
      final = f"{title} - {episode}.mkv"
    # final = f"{episode} - Noblesse [480p] [Dual] @AniVoid.mkv"
      #final = "{} - My Dress Up Darling [480p] [Dual] @AniVoid.mkv".format(episode)
      #final = final_.replace("Cleo", "")
    
  path = "downloads/"
  for i in os.listdir(path):
    folder_walk = os.walk(path)
    first_file_in_folder = next(folder_walk)[2][0]
    original = os.path.join(path, first_file_in_folder)
    new = os.path.join(path, final)
    os.rename(original, new)
  return final
    
    
async def rename_pro(bot, message):
  if_files = os.path.isdir("downloads/")
  if if_files == True:
   if os.listdir("downloads/") is not None:
    actual_files = os.listdir("downloads/")
    for i in actual_files:
     file_to_delete = "downloads/" + i
     os.remove(file_to_delete)
  download_location = Config.DOWNLOAD_LOCATION + "/"
  sent_message = await bot.send_message(
    text="**DOWNLOADING**",
    chat_id=message.chat.id,
    reply_to_message_id=message.message_id
  )
  c_time = time.time()
  f_n = await bot.download_media(
    message=message,
      #myDB.lindex("DBQueue", 0),
      #file_name=download_location,
    progress=progress_for_pyrogram,
    progress_args=(
      bot,
      "**DOWNLOADING**",
      sent_message,
      c_time
    )
  )
  logger.info(f"Starting to rename {f_n}")
  await asyncio.sleep(1)
  if f_n is not None:
    await sent_message.edit_text("**TRYING TO RENAME**")
    # if not .mkv or.mp4 or .webm
  if f_n.rsplit(".", 1)[-1].lower() not in ["mkv", "mp4", "webm", "avi"]:
    return await sent_message.edit_text("This format isnt allowed , please send only either **MKV** or **MP4** files.")
    # if in .mkv or .mp4
  #  real_file = 
  path = "downloads/"
  folder_walk = os.walk(path)
  first_file_in_folder = next(folder_walk)[2][0]
  _f_n = await anitopy_renamer(first_file_in_folder)
  new_file_name = "downloads/" + _f_n
  
  if _f_n is not None:
    await sent_message.edit_text(f"UPLOADING **{_f_n}** as a doc.")
    upload = await bot.send_document(
      chat_id=message.chat.id,
      document=new_file_name,
      force_document=True,
      #caption="©️ @Animes_Encoded",
      reply_to_message_id=message.message_id,
      progress=progress_for_pyrogram,
      progress_args=(bot, "UPLOADING", sent_message, c_time)
    )
      # remove uploaded file as it will free space
    _fn = "/root/encoder/downloads/" + _f_n
    os.remove(_fn)
    await sent_message.delete()
    
  

