# file for encode progress of ffmpeg 
from SmartEncoder.Tools.progress import *
from ethon.pyfunc import total_frames as tf
import asyncio
import subprocess 
import re
from SmartEncoder.__main__ import *
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


async def progress_shell(cmd, file, progress, now, message, ps_name):
  total_frames = tf(file)
  with open(progress, "w") as fk:
    pass
  proce = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
  while proce.returncode != 0:
    await asyncio.sleep(3)
    with open(progress, "r+") as fil:
      text = fil.read()
      frames = re.findall("frame=(\\d+)", text)
      size = re.findall("total_size=(\\d+)", text)
      speed = 0
      if len(frames):
        elapse = int(frames[-1])
      if len(size):
        size = int(size[-1])
        per = elapse * 100 / int(total_frames)
        time_diff = time.time() - int(now)
        speed = round(elapse / time_diff, 2)
      if int(speed) != 0:
        some_eta = ((int(total_frames) - elapse) / speed) * 1000
        perc = "{}%".format(round(per, 2))
        progress_str = "**[{0}{1}]**\n➖➖➖➖➖➖➖➖➖➖\n**PERCENTAGE:** {2}%".format(
          "".join("▣" for i in range(math.floor(per / 5))),
          "".join("□" for i in range(20 - math.floor(per / 5))),
          round(per, 2),
        )
        e_size = humanbytes((size / per) * 100)
        encoded_size = humanbytes(size)
        eta = TimeFormatter(some_eta)
        await message.edit_text(
         text = f'🏷 **Encoding in Progress**\n┏━━━━━━━━━━━━━━━━━ \n┣**Percentage** ➜ {perc}\n┣**Time Left** ➜ {eta}\n┣**Encoded Size** ➜ {encoded_size}\n┣**Estimated Size** ➜ {e_size}\n┗━━━━━━━━━━━━━━━━━',
          reply_markup=InlineKeyboardMarkup(
            [
              [
                InlineKeyboardButton("❌ CANCEL ❌", callback_data="cancel")],
            ],
          ),
        )
        
