import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

student_id = os.environ.get("STUDENT_ID")
password = os.environ.get("PASSWORD")
