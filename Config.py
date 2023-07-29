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

Config.AUTH_USERS = [1930343434, 5126929234]
Config.API_ID = 3281305
Config.API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
Config.BOT_TOKEN = "5125899321:AAHbONkOCPvl0_2u4OLe9Ofp8zTVpl7r8R4"
Config.REDIS_HOST = "redis-16314.c267.us-east-1-4.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "0nEnmigLRI1KjSDujhnekAQq2qFYZeQQ"
REDIS_PORT = "16314"
#.

#.
