# list.py>
"""
Python3 --> list
"""

from SmartEncoder.Database.db import myDB

class video:
  crf = []
  codec = []
  quality = []
  
  
#myDB.set('crf', "29.5")
video.codec.append("libx265")
video.quality.append("852x480")

class audio:
  a_bitrate = []
  a_codec = []

audio.a_bitrate.append("45k")
audio.a_codec.append("libopus")

class speed:
  preset = []

speed.preset.append("fast")

class watermark:
  size_one = []
  size_two = []

watermark.size_one.append('25')
watermark.size_two.append('30')
vanish = []
vanish.insert(0, "true")
#class queue:
#  data = []
#queue = []
name = []
name.append("480p")

rename_queue = []
rename_task = []
rename_task.insert(0, "off")

audio_ = []
quality_ = []
