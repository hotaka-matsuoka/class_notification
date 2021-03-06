import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

STUDENT_ID = os.environ["STUDENT_ID"]
PASSWORD = os.environ["PASSWORD"]
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["LINE_BOT_CHANNEL_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["LINE_BOT_CHANNEL_SECRET"]
USER_ID = os.environ["USER_ID"]
