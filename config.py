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
  DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "/app/downloads")

Config.AUTH_USERS = [6748415360]
Config.API_ID = 3847632
Config.API_HASH = "1a9708f807ddd06b10337f2091c67657"
Config.BOT_TOKEN = "6979551576:AAE35Fp2ui6XXyJ629EEN_ZXlpgaZsZgqzY"
Config.REDIS_HOST = "redis-19153.c10.us-east-1-2.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "f9Hstc2xMAI2FMGuLbGsn446LwsTM4c0"
REDIS_PORT = "19153"
Config.DOWNLOAD_LOCATION =  "/app/downloads"
#.

#.
