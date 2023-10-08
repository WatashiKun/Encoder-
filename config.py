import os
import dotenv
#import SmartEncoder.Database.db.myDB as db


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  GOD = os.environ.get("GOD")
  REDIS_HOST = os.environ.get("REDIS_HOST")
 # REDIS_PORT = int(os.environ.get("REDIS_PORT", 12345))
  REDIS_PASS = os.environ.get("REDIS_PASS")
  DOWNLOAD_LOCATION = "downloads"

Config.AUTH_USERS = [6440253535]
Config.API_ID = 3847632
Config.API_HASH = "1a9708f807ddd06b10337f2091c67657"
Config.BOT_TOKEN = "6431767198:AAGCX8GtdDRxbX3WOkDHkQxqyo64-BS-BiA"
Config.REDIS_HOST = "redis-12849.c84.us-east-1-2.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "7Sh7dHBfUEDvPdf1JLjty73JcN4omopO"
REDIS_PORT = "12849"
#.

#.
