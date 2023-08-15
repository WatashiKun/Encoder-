# encode.py> 

import asyncio
import os
import time
import subprocess
import math
import logging
logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

from SmartEncoder.Plugins.list import *

from SmartEncoder.Tools.progress import *
from SmartEncoder.Tools.ffmpeg_progress import progress_shell
from SmartEncoder.Database.db import myDB


async def en_co_de(dl, message):
  pron = dl.split("/")[-1]
  sox = pron.split(".")[-1]
  ul = pron.replace(f".{sox}", ".mkv")
  TF = time.time()
  progress = f"progress-{TF}.txt"
  # ffmpeg encoding code 
  if myDB.get('codec') == "libx265":
    if myDB.get("Audio_Codec") == "libfdk_aac":
      cmd = f'''ffmpeg -hide_banner -loglevel quiet -progress """{progress}""" -i """{dl}""" -filter_complex "drawtext=fontfile=njnaruto(1).ttf:fontsize={myDB.get("size")}:fontcolor=white:bordercolor=black@0.50:x={myDB.get("w_po")}:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text='Encode By AniVoid':enable='between(t,0,15)':alpha='if(lt(t,14)\,1\,if(lt(t\,15)\,(1-(t-14))/1\,0))'" -metadata:s:a:0 title="AniVoid" -metadata:s:a:1 title="AniVoid" -metadata:s:s:0 title="AniVoid" -metadata:s:s:1 title="AniVoid" -metadata title="Encode By AniVoid" -map 0:v? -map 0:a? -map 0:s? -c:v libx265 -x265-params no-info=1 -crf {myDB.get("crf")} -s {myDB.get("quality")} -b:v 420k  -preset {myDB.get('speed')} -threads 3 -pix_fmt yuv420p -tune animation -c:a libfdk_aac -profile:a aac_he_v2 -ac 2 -vbr 1 -c:s copy """{ul}""" -y'''
    elif myDB.get("Audio_Codec") == "libopus":
      cmd = f'''ffmpeg -hide_banner -loglevel quiet -progress """{progress}""" -i """{dl}""" -filter_complex "drawtext=fontfile=njnaruto(1).ttf:fontsize={myDB.get("size")}:fontcolor=white:bordercolor=black@0.50:x={myDB.get("w_po")}:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text='Encode By AniVoid':enable='between(t,0,15)':alpha='if(lt(t,14)\,1\,if(lt(t\,15)\,(1-(t-14))/1\,0))'" -metadata:s:a:0 title="AniVoid" -metadata:s:a:1 title="AniVoid" -metadata:s:s:0 title="AniVoid" -metadata:s:s:1 title="AniVoid" -metadata title="Encode By AniVoid" -map 0:v? -map 0:a? -map 0:s? -c:v libx265 -x265-params no-info=1 -crf {myDB.get("crf")} -s {myDB.get("quality")} -b:v 420k -preset {myDB.get("speed")} -threads 3 -pix_fmt yuv420p -tune animation -c:a libopus -profile:a aac_he -ac 2 -b:a 36k -c:s copy """{ul}""" -y'''
  else:
    if myDB.get("Audio_Codec") == "libopus":
      cmd = f'''ffmpeg -hide_banner -loglevel quiet -progress """{progress}""" -i """{dl}""" -filter_complex "drawtext=fontfile=njnaruto(1).ttf:fontsize={myDB.get("size")}:fontcolor=white:bordercolor=black@0.50:x=10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text='Encode By AniVoid':enable='between(t,0,15)':alpha='if(lt(t,14)\,1\,if(lt(t\,15)\,(1-(t-14))/1\,0))'" -metadata:s:a:0 title="AniVoid" -metadata:s:a:1 title="AniVoid" -metadata:s:s:0 title="AniVoid" -metadata:s:s:1 title="AniVoid" -map 0:a? -map 0:s? -map 0:v? -c:v libx264 -crf {myDB.get('crf')} -pix_fmt yuv420p -s {myDB.get('quality')} -preset {myDB.get("speed")} -c:a libopus -profile:a aac_he -ac 2 -b:a 36k -c:s copy """{ul}""" -y'''
    elif myDB.get("Audio_Codec") == "libfdk_aac":
      cmd = f'''ffmpeg -hide_banner -loglevel quiet -progress """{progress}""" -i """{dl}""" -filter_complex "drawtext=fontfile=njnaruto(1).ttf:fontsize={myDB.get("size")}:fontcolor=white:bordercolor=black@0.50:x=10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text='Encode By AniVoid':enable='between(t,0,15)':alpha='if(lt(t,14)\,1\,if(lt(t\,15)\,(1-(t-14))/1\,0))'" -metadata:s:a:0 title="AniVoid" -metadata:s:a:1 title="AniVoid" -metadata:s:s:0 title="AniVoid" -metadata:s:s:1 title="AniVoid" -map 0:a? -map 0:s? -map 0:v? -c:v libx264 -crf {myDB.get('crf')} -pix_fmt yuv420p -s {myDB.get('quality')} -preset {myDB.get("speed")} -c:a libfdk_aac -profile:a aac_he_v2 -ac 2 -vbr 1 -c:s copy """{ul}""" -y'''
  # bot pm info for process -_-
  await progress_shell(cmd, dl, progress, TF, message, "**ENCODING IN PROGRESS**")
  if os.path.lexists(ul):
    return ul
  else:
    return None
  
# (c) Animes_Encoded 
