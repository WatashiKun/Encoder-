# redis db 
import redis
from config import Config, REDIS_PORT

myDB = redis.Redis(
  host=Config.REDIS_HOST,
  port=REDIS_PORT,
  password=Config.REDIS_PASS,
  decode_responses=True
)
