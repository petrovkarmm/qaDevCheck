import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DEBUG = True

bot_test_token = os.getenv("BOT_TEST_TOKEN")
bot_token = os.getenv("BOT_TOKEN")

redis_connect_url = f"redis://:{os.getenv('REDIS_PASSWORD')}@redis:6379/0"

BOT_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
