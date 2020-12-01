import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

student_id = os.environ.get("STUDENT_ID")
password = os.environ.get("PASSWORD")
YOUR_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_BOT_CHANNEL_TOKEN")
YOUR_CHANNEL_SECRET = os.environ.get("LINE_BOT_CHANNEL_SECRET")
user_id = os.environ.get("USER_ID")
