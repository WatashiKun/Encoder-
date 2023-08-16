from SmartEncoder.__main__ import *
from pyrogram.types import CallbackQuery
from SmartEncoder.translation import Translation
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import Config
import psutil
import signal
#from SmartEncoder.Database.db import myDB 


async def cb_things(bot, update: CallbackQuery):
  if update.data == "hilp":
    await update.message.edit_text(
      text=Translation.HELP_TEXT,
      parse_mode="markdown",
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton("🔙", callback_data="beck")],
        ],
      )
    )
  elif update.data == "beck":
    await update.message.edit_text(
      text=Translation.START_TEXT, 
      parse_mode="markdown",
      reply_markup=InlineKeyboardMarkup(
        [
          [
            InlineKeyboardButton("📕Help", callback_data="hilp")],
        ],
      )
    )
  elif update.data == "cancel":
    if update.from_user.id in Config.AUTH_USERS:
      try:
        await update.message.delete()
        for proc in psutil.process_iter():
          processName = proc.name()
          processID = proc.pid
          if processName == "ffmpeg":
            os.kill(processID, signal.SIGKILL)
            #myDB.lpop("DBQueue")
      except:
        pass
      return
      
